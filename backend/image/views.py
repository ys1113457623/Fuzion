
from django.http import JsonResponse

import json
import requests
from fusion_backend.args import headers
from PIL import Image
from io import BytesIO


def classifyImage(request):
    query = request.GET.get('query','')
    API_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"
    response = requests.get(query)
    data = Image.open(BytesIO(response.content))
    
        
    response = requests.request("POST", API_URL, headers=headers, data=data)
    response = json.loads(response.content.decode("utf-8"))
    
    return JsonResponse(response,safe=False)

def ObjectDetection(request):
    query = request.GET.get('query','')
    API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
    response = requests.get(query)
    data = Image.open(BytesIO(response.content))
    
        
    response = requests.request("POST", API_URL, headers=headers, data=data)
    response = json.loads(response.content.decode("utf-8"))
    
    return JsonResponse(response,safe=False)

def imageDescription(request):
    query = request
    API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
    response = requests.get(query)
    # data = Image.open(BytesIO(response.content))
    
        
    response = requests.request("POST", API_URL, headers=headers, data=query)
    response = json.loads(response.content.decode("utf-8"))
    
    return JsonResponse(response,safe=False)


