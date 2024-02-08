from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re

# Create your views here.

def start_page(request):
    if request.method == "GET":
        context = {"message": "Welcome to the Hacker Fab Database"}
        return render(request, "home.html", context)

def search_page(request):
    '''if request.method == "GET":'''
    context = {"message": "Search Data here"}
    return render(request, "search.html", context)

def input_page(request):
    try:
        new_process = process_word_parameter(request.POST, "Process")
        context = compute_process_context(new_process)
    except Exception as e:
        process1 = {"id": f'Oxide Etch', "name": "Oxide Etch"}
        processes = [process1]
        context = {"processes": processes}
    return render(request, "input.html", context)

def process_word_parameter(req, word):
    return req[word]

def compute_process_context(process):
    if process == "Oxide Etch":
        measurements = []
        meas1 = {"id": "Glass Type", "name": "Glass Type", "values": [{"id": "P504", "name": "P504"}]}
        meas2 = {"id": "test2", "name": "test2"}
        measurements = [meas1, meas2]
        matrix = measurements
        process1 = {"id": f'Oxide Etch', "name": "Oxide Etch"}
        context = {"processes": process1, "matrix": matrix}
        return context