from django.shortcuts import render
from .models import AnswerModel,QuestionModel
from .pipelines import pipeline
import os
from urllib.parse import parse_qs
import json
from django.http import  JsonResponse
from PyPDF2 import PdfReader



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

    try:
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
    except Exception as e:
            return JsonResponse({"status":500,"error":str(e)})


def processDocumentPassage(passage_filename):
    text = ""
    paragraphs = []
    with open(passage_filename, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()

    # yktv
    paragraphs = text.split('\n\n')

    # na here i go split am into 400 words
    sub_paragraphs = []
    for paragraph in paragraphs:
        words = paragraph.split()
        sub_paragraph = ""
        for word in words:
            if len(sub_paragraph.split()) < 400:
                sub_paragraph += word + " "
            else:
                sub_paragraphs.append(sub_paragraph.strip())
                sub_paragraph = word + " "
        if sub_paragraph.strip():
            sub_paragraphs.append(sub_paragraph.strip())

    questions = []
    answers = []

    for one_para in sub_paragraph:
        response = np(str(one_para))
                
        for qa_pair in response:
            questions.append(qa_pair['question'])            
            answers.append(qa_pair['answer'])  
        
    return {"question":questions,"answer":answers}


    


