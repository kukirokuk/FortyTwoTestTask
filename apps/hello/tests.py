# -*- coding: utf-8 -*-

from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from django.http import HttpRequest

from apps.hello.views import home
from apps.hello.models import Contact
from apps.hello.forms import ContactForm


class HomePageTest(TestCase):

    def test_home_page_view(self):
        '''
         Check our view function for home page
        '''
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_correct_html(self):
        '''
         Check home page returns correct html
        '''
        request = HttpRequest()
        response = home(request)
        self.assertIn(b'42 Coffee Cups Test Assignment',
                      response.content)

        # check we've used the right template
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_from_fixture(self):
        '''
         Check home page displays data from fixture
        '''
        request = HttpRequest()
        response = home(request)

        # check our contact information appears on the page
        self.assertIn('Oleksandr', response.content.decode())
        self.assertIn('Vinnichuk', response.content.decode())

    def test_context(self):
        '''
        Check if right data is in context
        '''

        Contact.objects.all().delete()
        person = Contact()
        person.name = 'Oleksandr'
        person.save()
        response = self.client.get(reverse('home'))
        home_context = response.context['info']
        self.assertEqual(home_context, person)

    def test_cyrillic_render(self):
        '''
        Check if cyrillic render
        '''
        Contact.objects.all().delete()
        person = Contact()
        person.name = u'Олександр'
        person.save()
        response = self.client.get(reverse('home'))
        self.assertIn('Олександр', response.content)

    def test_all_fields_renders(self):
        '''
        Check if all fields from context renders
        '''
        Contact.objects.all().delete()
        person = Contact()
        person.name = 'Oleksandr'
        person.last_name = 'Vinnichuk'
        person.date_of_birth = '1984-06-13'
        person.skype = "prof.zojdberg"
        person.jabber = "kukirokuk@khavr.com"
        person.email = "oleksanr.v@gmail.com"
        person.other_contacts = "mobile +380664444032"
        person.bio = "Born in Kovel"
        person.save()
        response = self.client.get(reverse('home'))
        self.assertIn('Oleksandr', response.content)
        self.assertIn('Vinnichuk', response.content)
        self.assertIn('June 13, 1984', response.content)
        self.assertIn('prof.zojdberg', response.content)
        self.assertIn('kukirokuk@khavr.com', response.content)
        self.assertIn('kukirokuk@khavr.com', response.content)
        self.assertIn('oleksanr.v@gmail.com', response.content)
        self.assertIn('mobile +380664444032', response.content)
        self.assertIn('Born in Kovel', response.content)

    def test_multiple_db_instances(self):
        '''
        Check if db has more then one instances, the first one is
        rendered
        '''
        Contact.objects.all().delete()
        person1 = Contact()
        person1.name = "Pablo"
        person1.save()
        person2 = Contact()
        person2.name = "Juan"
        person2.save()
        response = self.client.get(reverse('home'))
        home_context = response.context['info']
        self.assertEqual(home_context, person1)

    def test_empty_db(self):
        '''
        Check if db is empty
        '''
        Contact.objects.all().delete()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class ContactModelTest(TestCase):

    def test_saving_fields(self):
        '''
         Check model can save data
        '''
        person = Contact()
        person.name = 'Petro'
        person.last_name = 'Shchur'
        person.save()

        # check our model saves data
        saved_persons = Contact.objects.all()
        self.assertEqual(saved_persons.count(), 2)
        person_from_fixtures = saved_persons[0]
        saved_person = saved_persons[1]
        self.assertEqual(saved_person.name, 'Petro')
        self.assertEqual(saved_person.last_name, 'Shchur')
        self.assertEqual(person_from_fixtures.name, 'Oleksandr')
        self.assertEqual(person_from_fixtures.last_name, 'Vinnichuk')


class ContactEditFormTest(TestCase):

    def setUp(self):
        # Contact.objects.all().delete()
        self.url = reverse('user_detail')
        self.data = {
            'name': 'Pablo',
            'last_name': 'Escobar',
            'date_of_birth': '1949-12-01',
            'skype': 'pablito',
            'jabber': 'pablito@khavr.com',
            'email': 'pablo.e@gmail.com',
            'other_contacts': 'mobile +79023405442',
            'bio': 'Born in Antioquia, Colombia'}

    def test_form_fields(self):
        '''
         Check form
        '''
        # login as admin to access student edit form
        self.client.login(username='admin', password='admin')

        self.response = self.client.get(self.url)

        # check response status
        self.assertEqual(self.response.status_code, 200)

        # check form fields
        self.assertIn('name="name"', self.response.content)
        self.assertIn('name="last_name"', self.response.content)
        self.assertIn('name="date_of_birth"', self.response.content)
        self.assertIn('name="email"', self.response.content)
        self.assertIn('name="jabber"', self.response.content)
        self.assertIn('name="other_contacts"', self.response.content)
        self.assertIn('name="bio"', self.response.content)
        self.assertIn('name="image"', self.response.content)
        self.assertIn('action="%s"' % self.url,
                      self.response.content)

    def test_post(self):
        '''
         Check form saves data
        '''
        # login as admin to access student edit form
        self.client.login(username='admin', password='admin')

        # check response status
        self.response = self.client.post(self.url, self.data)
        self.assertEqual(self.response.status_code, 200)

        # test updated model saved data from post
        person = Contact.objects.get(pk=1)
        self.assertEqual(person.name, self.data['name'])
        self.assertEqual(person.last_name, self.data['last_name'])

    def test_auth(self):
        '''
         Check authentication works properly
        '''
        # access as anonymous user
        response = self.client.get(self.url, follow=True)

        # check that we are on login form
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login for profile data edit', response.content)

    def test_ajax(self):
        '''
         Check ajax
        '''
        # login as admin to access student edit form
        self.client.login(username='admin', password='admin')

        # check ajax get request
        kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        response = self.client.get(reverse('user_detail'), **kwargs)
        self.assertEquals(response.status_code, 200)

        # check ajax valid post request with all required fields filled
        response = self.client.post(reverse('user_detail'),
                                    self.data, **kwargs)
        self.assertEquals(response.status_code, 200)
        person = Contact.objects.get(pk=1)
        self.assertEqual(person.name, self.data['name'])
        self.assertEqual(person.last_name, self.data['last_name'])

        # check invalid post request with missed ruqeired fields
        response = self.client.post(reverse('user_detail'),
                                    {'name': 'Juan',
                                    'last_name': ''}, **kwargs)
        self.assertEquals(response.status_code, 200)
        person = Contact.objects.get(pk=1)
        self.assertNotEquals(person.name, 'Juan')

    def test_valid_invalid_form(self):
        '''
         Check form validation
        '''

        # login as admin to access student edit form
        self.client.login(username='admin', password='admin')

        # test valid form with all required fields added
        person = Contact.objects.create(
            name=self.data['name'],
            last_name=self.data['last_name'],
            jabber=self.data['jabber'],
            skype=self.data['skype'])
        form = ContactForm(data={
            'name': person.name,
            'last_name': person.last_name,
            'jabber': person.jabber,
            'skype': person.skype})
        self.assertTrue(form.is_valid())

        Contact.objects.all().delete()

        # test valid form with one required fields missed
        person = Contact.objects.create(
            name=self.data['name'],
            last_name=self.data['last_name'],
            jabber=self.data['jabber'])
        form = ContactForm(data={
            'name': person.name,
            'last_name': person.last_name,
            'jabber': person.jabber})
        self.assertFalse(form.is_valid())

    def test_widget(self):
        '''
         Check widget appear at contact edit page
        '''

        # login as admin to access student edit form
        self.client.login(username='admin', password='admin')

        # test widget appear at form page
        response = self.client.get(reverse('user_detail'))
        self.assertIn('<a href="/">Cancel</a>', response.content)
