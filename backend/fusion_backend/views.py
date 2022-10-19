from django.http import HttpResponse

import text.views as text
import image.views as image 



# class GenerateSocialCaption:
#     def __init__(self) -> None:
        
# Defining a function which
# will receive request and
# perform task depending
# upon function definition
def generateSocialCaption(request):
    # Get the request type
    # and perform task
    # accordingly
    if request.method == 'GET':
        return text.generateSocialCaption(request)
    elif request.method == 'POST':
        return HttpResponse("POST")
    elif request.method == 'PUT':
        return HttpResponse("PUT")
    elif request.method == 'DELETE':
        return HttpResponse("DELETE")
    else:
        return HttpResponse("Invalid Request")

