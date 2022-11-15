from datetime import datetime
from django.db import models

class CandidateInfo(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    time_to_call = models.DateTimeField(default=datetime.now)
    linkedin_url = models.CharField(max_length=100)
    github_url = models.CharField(max_length=100)
    free_text_comments = models.TextField()

    def __str__(self):
        return self.email
    

    class Meta:
        verbose_name_plural = 'Candidate Info'
    


