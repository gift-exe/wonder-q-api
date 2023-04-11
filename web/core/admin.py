from django.contrib import admin
from .models import QuestionModel,AnswerModel

# Register your models here.
admin.site.register(QuestionModel)
admin.site.register(AnswerModel)