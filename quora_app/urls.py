from django.urls import path, include

from quora_app.views import (
    QuestionListAPIView, 
    QuestionDetailsAPIView,
    AnswerListAPIView, 
    AnswerLikeAPIView,
)

urlpatterns = [
    # to get question list or for creating question
    path('questions/', QuestionListAPIView.as_view(), name="question_lists"),
    
    # to get specific question by its id
    path('questions/<int:pk>/', QuestionDetailsAPIView.as_view(), name='question_details'),
    
    # to get the answers for the specific question and to post the answer
    path('questions/<int:id>/answers/', AnswerListAPIView.as_view(), name='answer_lists'),
    
    # for like functionality
    path('answers/<int:pk>/likes/', AnswerLikeAPIView.as_view(), name='answer_likes'),
]


