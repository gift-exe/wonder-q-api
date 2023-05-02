from django.shortcuts import render
from .models import AnswerModel,QuestionModel


# Create your views here.



def index(request):
    return render(request,'core/home.html')


def details_page(request):
    query_obj = AnswerModel.objects.all()
    context = {
        "questions":query_obj
    }
    return render(request,'core/details.html',context)


#taskss
#topic and level of difficulty
#number of questions they want
#save questions and options to print as pdf ----