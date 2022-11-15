from rest_framework import serializers
from .models import CandidateInfo

class CandidateInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CandidateInfo
        fields = '__all__'
       
   