from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Poll, Choice, Vote, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        email = validated_data['email']
        #username=validated_data['username']
        # if email and User.objects.filter(email=email).exists():
        #     return 'Email addresses must be unique.'
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields ='__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'
class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    
    class Meta:
        model = Poll
        fields = '__all__'
