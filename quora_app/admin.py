from django.contrib import admin
from quora_app.models import Question, Answer

# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)