from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.views import add_candidate_information, update_candidate_information


class apiUrlTestCase(SimpleTestCase):

    def test_add_information_url(self):
        url = reverse('add_info')
        self.assertEquals(resolve(url).func,  add_candidate_information)


    def test_update_information_url(self):
        url = reverse('update_info', args=['1'])
        self.assertEquals(resolve(url).func,  update_candidate_information)

