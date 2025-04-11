from rest_framework import serializers
from quora_app.models import Question,Answer
from django.contrib.auth.models import User

'''
User Serializer for user model using Model serializer
'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        

'''
Answer Serializer for user model using Model serializer
'''
class AnswerSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    likes = serializers.IntegerField(source='like_count', read_only=True)
    class Meta:
        model = Answer
        fields = '__all__'


'''
Question Serializer for user model using Model serializer
'''    
class QuestionSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    answers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Question
        fields = '__all__'
        