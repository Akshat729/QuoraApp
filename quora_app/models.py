from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

'''
class to initialize Question model
'''
class Question(models.Model):
    content = models.TextField()                                                        # question content
    category = models.CharField(max_length=50)                                          # question category
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions") # user who post the question
    creation_date = models.DateTimeField(auto_now=True)                                 # creation date when user post the question
    active = models.BooleanField(default=True)                                          # it shows question is active or not
    
    # function to return the question content
    def __str__(self):
        return self.content

'''
class to initialize Answer model
'''
class Answer(models.Model):
    content = models.TextField()                                                                    # answer content
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")              # user who answer the question
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")       # question for which user gives the answer
    creation_date = models.DateTimeField(auto_now=True)                                             # creation date when user post the answer
    likes = models.ManyToManyField(User, related_name="likes")                                      # like count
    
    # function to return the answer content
    def __str__(self):
        return self.content
    
    # function to return the like count
    def like_count(self):
        return self.likes.count()

    
    
