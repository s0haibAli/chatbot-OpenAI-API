from django.shortcuts import render, HttpResponse
from django.http import JsonResponse 

import os
import openai

#Setting up key to access and use the OpenAI API services (put API key here)
openai.api_key = ""

# Create your views here.
# Function to show "index.html" page to user
def chat(request):
    return render(request, "index.html")

# Function to show "about.html" page to user
def about(request):
    return render(request, "about.html")

def chatAPI(request):
    #If request is POST
    if request.method == "POST":
        #Retrieve the value of the "prompt" field from the request's POST data and put that into prompt variable 
        prompt = request.POST["prompt"]
        #Send completion request to OpenAI API using the openai.Completion.create() method
        #Provides necessary parameters for the completion, like model to use, prompt text, and options like temperature, max tokens, and penalties
        #Method returns a response object from the OpenAI API
        response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.7, max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0)
        #Returns a JSON response containing the response object obtained from the OpenAI API
        return JsonResponse(response)
    
    #If not POST, return "Bad request"
    return HttpResponse("Bad request")