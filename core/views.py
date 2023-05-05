from django.shortcuts import render
from .models import AnswerModel,QuestionModel
# from .pipelines import pipeline


# Create your views here.



def index(request):
    
    if request.method == 'POST':
        

        #extract the required 
        context = request.POST.post('context')
        passage = request.POST.post('passage')
    
        #init the models
        np = pipeline("multitask-qa-qg")

        response = np(str(passage))
        
        print(response)

        #here down ...experimental, might not work, have not tested
        question = QuestionModel(
            question=response['question']
            
        )
        question.save()

        answer = AnswerModel(
            question=question,
            answer=response['answer']
        )

        answer.save()

        context = {"question":response['question'],
                    "answer":response['answer']
        
        }
        return render(request,'core/details.html',context)

    return render(request,'core/home.html')


def details_page(request):
    query_obj = AnswerModel.objects.all()
    context = {
        "questions":query_obj
    }
    return render(request,'core/more.html',context)


#taskss
#topic and level of difficulty
#number of questions they want
#save questions and options to print as pdf ----