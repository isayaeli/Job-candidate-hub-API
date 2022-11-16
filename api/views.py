
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.models import CandidateInfo
from api.serializers import CandidateInfoSerializer
from drf_yasg.utils import swagger_auto_schema


#this function below is responsible for adding  candidates information.

@swagger_auto_schema(method='POST', request_body=CandidateInfoSerializer)
@api_view(['POST',])
def add_candidate_information(request):

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


#this function below is responsible for updating candidates information if their profile exists

@swagger_auto_schema(method='PUT', request_body=CandidateInfoSerializer)
@api_view(['PUT',])
def update_candidate_information(request, pk):

    try:
        candidate = CandidateInfo.objects.get(pk=pk)
    except candidate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CandidateInfoSerializer(candidate, data=request.data)
        data = {}
        if serializer.is_valid():
            candidate = serializer.save()
            data['response'] = "Successful Updated candidate info"
            data['first_name'] = candidate.first_name
            data['last_name'] = candidate.last_name
            data['candidateId'] = candidate.id
        else:
            data = serializer.errors
        return Response(data)
    