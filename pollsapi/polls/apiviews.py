from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework import serializers

from .models import Poll, Choice, User, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer

from django.contrib.auth import authenticate

class LoginView(viewsets.ViewSet):
    
    serializer_class = AuthTokenSerializer

    def create(self, request):
 
        return ObtainAuthToken().post(request)


class UserCreate(generics.CreateAPIView):
    #To use CreateAPIView Only you the commented style below, though it works fine with just querry_set too
    # authentication_classes = ()
    # permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
   
    def get_queryset(self):
        queryset = Choice.objects.all()
        return queryset
    serializer_class = ChoiceSerializer

class CreateVote(generics.ListCreateAPIView):

    def get_queryset(self):
        query_set = Vote.objects.all()
        return query_set
    serializer_class = VoteSerializer

    # def post(self, request, pk, choice_pk):
    #     voted_by = request.data.get("voted_by")
    #     data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
    #     serializer_class= VoteSerializer(data=data)
    #     if serializer_class.is_valid():
    #         vote = serializer_class.save()
    #         return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)





# from rest_framework.views import APIView
# from rest_framework.response import Response

# from django.shortcuts import get_object_or_404

# from .models import Poll, Choice
# from .serializers import PollSerializer

# class PollList(APIView):
    
#     def get(self, request):
#         polls = Poll.objects.all()[:20]
#         data = PollSerializer(polls, many=True).data
#         return Response(data)

# class PollDetail(APIView):

#     def get(self, request, pk):
#         poll = get_object_or_404(Poll, pk=pk)
#         data = PollSerializer(poll).data
#         return Response(data)