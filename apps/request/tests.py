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
