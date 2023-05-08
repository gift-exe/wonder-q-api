from django.shortcuts import render
from .models import AnswerModel,QuestionModel
from .pipelines import pipeline
import os
from urllib.parse import parse_qs
import json
from django.http import  JsonResponse


np = pipeline('multitask-qa-qg')

def index(request):

    if request.method == 'POST':
        
        #extract the required 
        passage = request.POST.get('passage')

        response = np(str(passage))
        

        #here down ...experimental, might not work, have not tested
        questions = []
        answers = []
        for qa_pair in response:

            questions.append(qa_pair['question'])            
            answers.append(qa_pair['answer'])

        
        return render(request,'core/details.html',{"questions":questions, "answers":answers})

    return render(request,'core/home.html')


def details_page(request):

    return render(request,'core/details.html')


def processPassage(request):
    form_data = request.body
    form_dict = parse_qs(form_data.decode('utf-8'))
    passage = form_dict.get('passage', [''])[0]
    
    questions = []
    answers = []

    response = np(str(passage))
        
    for qa_pair in response:
        questions.append(qa_pair['question'])            
        answers.append(qa_pair['answer'])        
    return JsonResponse({"status":200,"questions":questions, "answers":answers})
