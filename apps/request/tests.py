from django.test import TestCase
from django.core.urlresolvers import reverse


from apps.request.models import SavedRequest


class RequestPageTest(TestCase):

    def test_middleware(self):
        '''
         Check stored requests page and model
        '''
        response = self.client.get(reverse('requests'))

        # check template
        self.assertTemplateUsed(response, 'show_requests.html')

        # check responce status
        self.assertEqual(response.status_code, 200)

        # check model
        req = SavedRequest.objects.get(path=response.request["PATH_INFO"])

        # check model instance rendered
        self.assertIn(req.path, response.content)

    def test_last_ten_requests(self):
        '''
         Check page shows last 10 requests
        '''
        url = reverse('requests')

        # creating 10 requests
        for i in range(10):
            request = self.client.get(url)

        test_requests = list(SavedRequest.objects.all().order_by('-id')[:10])

        # check if last requests appear at the page
        for t_request in test_requests:
            self.assertIn(t_request, request.context['requests'])

    def test_with_priority_request(self):
        '''
        Check page shows up requests sorted by priority
        '''
        # making names for requests
        requests = ['request'+str(i) for i in range(10)]

        # iterate over different priorities
        for pr in range(1, 3):
            # creating 10 new requests with priority
            for request in requests:
                request = SavedRequest(priority=pr)
                request.save()

            tr = list(SavedRequest.objects.filter(priority=pr).order_by('-id'))
            test_requests = tr[:10]
            response = self.client.get(reverse('requests')+"?order_by=" +
                                       str(pr))
            # check if last requests with specified priority appear at the page
            for t_request in test_requests:
                self.assertIn(t_request, response.context['requests'])
