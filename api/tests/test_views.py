from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.views import add_candidate_information, update_candidate_information
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import CandidateInfo

class ApiViewsTestCase(APITestCase):

    data = {
        "email": "isaya@example.com",
        "first_name": "Isaya",
        "last_name": "Bendera",
        "phone": "0684695157",
        "time_to_call": "from 09am - 23pm",
        "linkedin_url": "linkedin.com/isayabendera",
        "github_url": "github.com/isayaeli",
        "free_text_comments": "No comments foe now"
    }

    ivalid_data = {
            "email": "",
            "first_name": "Isaya",
            "last_name": "Bendera",
            "phone": "0684695157",
            "time_to_call": "from 09am - 23pm",
            "linkedin_url": "linkedin.com/isayabendera",
            "github_url": "github.com/isayaeli",
            "free_text_comments": "No comments foe now"
        }

    def test_add_candidate_infomation_view(self):
        url = reverse('add_info')
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    

    def test_invalid_add_candidate_infomation_view(self):
        url = reverse('add_info')
        response = self.client.post(url, self.ivalid_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


   

    def test_update_candidate_infomation_view(self):
        candidate_info = CandidateInfo.objects.create(email='isaya@gmail.com.com', first_name='isaya',
        last_name='bendera',phone='22222',time_to_call = 'nytime',linkedin_url='www.com', github_url='www.com',
        free_text_comments='commets')

        url = reverse('update_info', kwargs={'pk': candidate_info.pk})
        response = self.client.put(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_invalid_update_candidate_infomation_view(self):
        candidate_info = CandidateInfo.objects.create(email='isaya@gmail.com.com', first_name='isaya',
        last_name='bendera',phone='22222',time_to_call = 'nytime',linkedin_url='www.com', github_url='www.com',
        free_text_comments='commets')

        url = reverse('update_info', kwargs={'pk': candidate_info.pk})
        response = self.client.put(url, self.ivalid_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)