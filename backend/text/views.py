
from django.http import JsonResponse

from .models import TextModel
import json
import requests
from fusion_backend.args import headers


 
def index(request):
  return JsonResponse("Hello text")

def missWord(request):
    query = request.GET.get('query','')
    payload = {"inputs": query.replace('?','[MASK]')}
    API_URL = "https://api-inference.huggingface.co/models/bert-base-uncased"
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    response = json.loads(response.content.decode("utf-8"))
    
    a = TextModel(query = query,response=response)
    a.save()
    
    return JsonResponse(response,safe=False)


def summarize(request):
    query = request.GET.get('query','')
    payload = {"inputs": query,"parameters":{"do_sample":False}}
    
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    response = json.loads(response.content.decode("utf-8"))
    
    a = TextModel(query = query,response=response)
    a.save()
    
    return JsonResponse(response,safe=False)

def questionAns(request):
    query = request.GET.get('query','')
    context = request.GET.get('context','')
    payload = {"inputs": {"question":query,"context":context}}
    
    API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    response = json.loads(response.content.decode("utf-8"))
    
    a = TextModel(query = query,response=response)
    a.save()
    
    return JsonResponse(response,safe=False)

def sentiment(request):
    query = request.GET.get('query','')
    payload = {"inputs": query}
    API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    response = json.loads(response.content.decode("utf-8"))
    
    a = TextModel(query = query,response=response)
    a.save()
    
    return JsonResponse(response,safe=False)

def textGen(request):
    query = request.GET.get('query','')
    payload = {"inputs": query}
    API_URL = "https://api-inference.huggingface.co/models/gpt2"
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    response = json.loads(response.content.decode("utf-8"))
    
    a = TextModel(query = query,response=response)
    a.save()
    
    return JsonResponse(response,safe=False)

def tokenClass(request):
    query = request.GET.get('query','')
    payload = {"inputs": query,"wait_for_model":True}
    API_URL =  "https://api-inference.huggingface.co/models/dbmdz/bert-large-cased-finetuned-conll03-english"
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    response = json.loads(response.content.decode("utf-8"))
    
    a = TextModel(query = query,response=response)
    a.save()
    
    return JsonResponse(response,safe=False)

def converse(request):
    query = request.GET.get('query','')
    past_user_inputs = request.GET.get('past_user_inputs','')
    generated_responses = request.GET.get('generated_responses','')
    
    payload = {"inputs": {"past_user_inputs":[past_user_inputs],"generated_responses":[generated_responses],"text":query},"wait_for_model":True}
    API_URL =  "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    response = json.loads(response.content.decode("utf-8"))
    
    a = TextModel(query = query,response=response)
    a.save()
    
    return JsonResponse(response,safe=False)