from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re
import json

def get_processes():
    processes = []
    with open('headers.json') as json_file:
        json_dict = json.load(json_file)
    for key in json_dict:
        process = {"id": f'{key}', "name": f'{key}'}
        processes.append(process)
    return processes

def get_meas(processes):
    measurements = []
    with open('headers.json') as json_file:
        json_dict = json.load(json_file)
    for process in processes:
        process_values = json_dict[process]
        for key in process_values:
            values = []
            for name in process_values[key]:
                value = {"id": f'{name}', "name": f'{name}'}
                values.append(value)
            meas = {"id": f'{key}', "name": f'{process} {key}', "values": values}
            measurements.append(meas)
    return measurements

# Create your views here.

def start_page(request):
    context = {"message": "Welcome to the Hacker Fab Database"}
    return render(request, "home.html", context)

def search_page(request):
    try:
        context = compute_search_context(request.POST)
    except Exception as e:
        processes = get_processes()
        context = {"message": "Search Data here", "processes": processes}
    return render(request, "search.html", context)

def input_page(request):
    try:
        new_process = process_input(request.POST, "Process")
        context = compute_input_context(new_process)
    except Exception as e:
        processes = get_processes()
        context = {"message": "Input Data here","processes": processes}
    return render(request, "input.html", context)

def process_input(req, word):
    return req[word]

def compute_input_context(process):
    measurements = get_meas([process])
    processes = get_processes()
    context = {"processes": processes, "matrix": measurements}
    return context

def process_search(req):
    rel_processes = []
    for key, value in req.lists():
        k = key[1:]
        rel_processes.append(k)
    rel_processes = rel_processes[:-1]
    return rel_processes

def compute_search_context(req):
    processes = get_processes()
    rel_processes = process_search(req)
    measurements = get_meas(rel_processes)
    context = {"message": "Search Data here", "processes": processes, "matrix": measurements}
    return context