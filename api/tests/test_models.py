from django.test import TestCase
from api.models import CandidateInfo

class CandidateInfoTestCase(TestCase):

    def create_candidate_info(self, email='isaya@gmail.com.com', first_name='isaya',
        last_name='bendera',phone='22222',time_to_call = 'nytime',linkedin_url='www.com', github_url='www.com',
        free_text_comments='commets'):
        return CandidateInfo.objects.create(email=email, first_name=first_name,
        last_name=last_name,phone=phone,time_to_call = time_to_call,linkedin_url=linkedin_url, github_url= github_url,
        free_text_comments=free_text_comments)

    def test_candidate_info_creation(self):
        candidate = self.create_candidate_info()
        self.assertTrue(isinstance(candidate, CandidateInfo))
        self.assertEqual(candidate.__str__(), candidate.email)