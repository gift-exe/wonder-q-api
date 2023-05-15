from urllib.parse import parse_qs
import json
from PyPDF2 import PdfReader
from pipelines import pipeline

np = pipeline('multitask-qa-qg')



async def processPassage(passage:str):

    try:
        
        questions = []
        answers = []

        response = np(str(passage))
            
        for qa_pair in response:
            questions.append(qa_pair['question'])            
            answers.append(qa_pair['answer'])        
        return {"status":200,"questions":questions, "answers":answers}
    except Exception as e:
            return {"status":500,"error":str(e)}


async def processLongPassage(passage: str):

    try:
        paragraphs = passage.split('\n')
        # omo tktv
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
        # process one after the other
        for one_para in sub_paragraphs:
            response = np(str(one_para))
            for qa_pair in response:
                question = qa_pair['question']
                answer = qa_pair['answer']
                questions.append(question)
                answers.append(answer)

        return {"status": 200, "questions": questions, "answers": answers}
    except Exception as e:
        return {"status": 500, "error": str(e)}





async def processDocumentPassage(passage_filename):
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

    # process one after the other
    for one_para in sub_paragraphs:
        response = np(str(one_para))
        for qa_pair in response:
            question = qa_pair['question']
            answer = qa_pair['answer']
            questions.append(question)
            answers.append(answer)
        
    return {"question":questions,"answer":answers}
