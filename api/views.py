
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import CandidateInfoSerializer
# Create your views here.

@api_view(['POST',])
def add_candidate_info(request):
    if request.method == 'POST':
        serializer = CandidateInfoSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            candidate = serializer.save()
            data['response'] = "Successful Added candidate info"
            data['first_name'] = candidate.first_name
            data['last_name'] = candidate.last_name
            data['candidateId'] = candidate.id
        else:
            data = serializer.errors
        return Response(data)