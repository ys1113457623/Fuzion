from django.http import HttpResponse

import text.views as text
import image.views as image 

# Defining a function which
# will receive request and
# perform task depending
# upon function definition
def whichModel(request) :
    # This will return Hello Geeks
    # string as HttpResponse
    return HttpResponse("Hello")

