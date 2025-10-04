from django.shortcuts import render
from quora_app.models import Answer, Question
from quora_app.serailizers import QuestionSerializer, AnswerSerializer
from rest_framework.views import APIView 
from rest_framework import permissions
from rest_framework.response import Response
 
# Create your views here.

'''
To get the list of all questions 
and to post the question
'''
class QuestionListAPIView(APIView):
    
    # only authenticated user can post the question other user will be able only read the questions
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
    
    #post function to ask the questions
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
'''
To get the specific question
'''
class QuestionDetailsAPIView(APIView):
    
    # only authenticated user can get the question other user will be able only read the questions
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
            serializer = QuestionSerializer(question)
            return Response(serializer.data, status=200)
        except Question.DoesNotExist:
            return Response({"error": "Question not found!"}, status=400)

    
'''
To get the list of all answers posted 
and to post the question to a specific question 
'''
class AnswerListAPIView(APIView):
    
    # only authenticated user can post the answer other user will be able to read the answers posted by others    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        answer = Answer.objects.filter(questions=id)
        serializer = AnswerSerializer(answer, many=True)
        return Response(serializer.data)
    
    def post(self, request, id):
        try:
            question = Question.objects.get(id=id)
            
            # author can not answer its own question
            if question.author==request.user:
                
                # otherwise raise error
                return Response({"error": "You can not answer your question!"}, status=204)
            
            # if auestion is active then only can give answer
            if question.active:
                serializer = AnswerSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save(author=request.user, question=question)
                    return Response(serializer.data, status=201)
                return Response(serializer.errors, status=400)
            
            # otherwise raise error
            return Response({"error": "Question has been closed!"}, status=204)
        
        # if question not exist raise error
        except Question.DoesNotExist:
            return Response(serializer.errors, status=400)

'''
class for functionality to like an answer or remove like
'''
class AnswerLikeAPIView(APIView):
    # only authenticated user can like the answer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        try:
            answer = Answer.objects.get(pk=pk)
            user = request.user
            
            # if user already likes the answer then remove
            if user in answer.likes.all():
                answer.likes.remove(user)
            # otherwise add the user 
            else:
                answer.likes.add(user)   
            # returning the like count   
            return Response({"like_count": answer.like_count()}, status=200)
        # if answer does not exist raise the error
        except Answer.DoesNotExist:
            return Response({"error": "Answer not found!"}, status=400)
