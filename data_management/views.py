from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re
import json
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.utils import timezone

from data_management.forms import LoginForm, RegisterForm, AluminumEtchForm, AluminumEvaporationForm, ChipListForm, DepositionTemplateForm, OxideEtchForm, PatterningForm, PlasmaCleanForm, PlasmaEtchForm
from data_management.models import AluminumEtch, AluminumEvaporation, ChipList, DepositionTemplate, OxideEtch, Patterning, PlasmaClean, PlasmaEtch
from data_management.forms import AluminumEtchSearchForm, AluminumEvaporationSearchForm, DepositionTemplateSearchForm, OxideEtchSearchForm, PatterningSearchForm, PlasmaCleanSearchForm, PlasmaEtchSearchForm

def get_processes():
    processes = []
    with open('headers.json') as json_file:
        json_dict = json.load(json_file)
    for key in json_dict:
        process = {"id": f'{key}', "name": f'{key}'}
        processes.append(process)
    return processes

def get_input_meas(processes):
    forms = []
    for process in processes:
        if process == "Aluminum Etch":
            form = AluminumEtchForm()
        if process == "Aluminum Evaporation":
            form = AluminumEvaporationForm()
        if process == "Deposition":
            form = DepositionTemplateForm()
        if process == "Oxide Etch":
            form = OxideEtchForm()
        if process == "Patterning":
            form = PatterningForm()
        if process == "Plasma Clean":
            form = PlasmaCleanForm()
        if process == "Plasma Etch":
            form = PlasmaEtchForm()
        f = {"name": f'{process}', "form": form}
        forms.append(f)
    return forms

def get_search_meas(processes):
    forms = []
    for process in processes:
        if process == "Aluminum Etch":
            form = AluminumEtchSearchForm()
        if process == "Aluminum Evaporation":
            form = AluminumEvaporationSearchForm()
        if process == "Deposition":
            form = DepositionTemplateSearchForm()
        if process == "Oxide Etch":
            form = OxideEtchSearchForm()
        if process == "Patterning":
            form = PatterningSearchForm()
        if process == "Plasma Clean":
            form = PlasmaCleanSearchForm()
        if process == "Plasma Etch":
            form = PlasmaEtchSearchForm()
        f = {"name": f'{process}', "form": form}
        forms.append(f)
    return forms

def save_form(processes, request):
    for process in processes:
        if process == "Aluminum Etch":
            form = AluminumEtchForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            new_model = AluminumEtch(chip_number=request.POST['chip_number'], alum_etch_temp=request.POST['alum_etch_temp'], alum_etch_time=request.POST['alum_etch_time'], stir_rpm=request.POST['stir_rpm'], metric_alum_etch_depth=request.POST['metric_alum_etch_depth'], metric_photoresist_peeling=request.POST['metric_photoresist_peeling'], metric_aluminum_peeling=request.POST['metric_aluminum_peeling'], metrology_link=request.POST['metrology_link'], notes=request.POST['notes'], chip_owner=request.user, creation_time=timezone.now())
            new_model.save()
        if process == "Aluminum Evaporation":
            form = AluminumEvaporationForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            new_model = AluminumEvaporation(chip_number=request.POST['chip_number'], aluminum_evaporation_temp=request.POST['aluminum_evaporation_temp'], aluminum_evaporation_time=request.POST['aluminum_evaporation_time'], pressure_before_start_seq=request.POST['pressure_before_start_seq'], pressure_before_evaporation=request.POST['pressure_before_evaporation'], metric_layer_thickness=request.POST['metric_layer_thickness'], metric_layer_thick_qcm=request.POST['metric_layer_thick_qcm'], metric_deposition_rate=request.POST['metric_deposition_rate'], metrology_link=request.POST['metrology_link'], notes=request.POST['notes'], chip_owner=request.user, creation_time=timezone.now())
            new_model.save()
        if process == "Deposition":
            form = DepositionTemplateForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            new_model = DepositionTemplate(chip_number=request.POST['chip_number'], glass_type=request.POST['glass_type'], cleaning_step=request.POST['cleaning_step'], days_glass_at_room_temp=request.POST['days_glass_at_room_temp'], prebake_temp=request.POST['prebake_temp'], prebake_time=request.POST['prebake_time'], amount_drops=request.POST['amount_drops'], spin_rpm=request.POST['spin_rpm'], spin_time=request.POST['spin_time'], bake_temp=request.POST['bake_temp'], bake_time=request.POST['bake_time'], humidity=request.POST['humidity'], metric_layer_thickness=request.POST['metric_layer_thickness'], metric_cracking=request.POST['metric_cracking'], metric_particles=request.POST['metric_particles'], metrology_link=request.POST['metrology_link'], notes=request.POST['notes'], chip_owner=request.user, creation_time=timezone.now())
            new_model.save()
        if process == "Oxide Etch":
            form = OxideEtchForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            new_model = OxideEtch(chip_number=request.POST['chip_number'], max_temp_glass_reached=request.POST['max_temp_glass_reached'], oxide_etch_time=request.POST['oxide_etch_time'], oxide_etch_temp=request.POST['oxide_etch_temp'], metric_oxide_etch_depth=request.POST['metric_oxide_etch_depth'], metrology_link=request.POST['metrology_link'], notes=request.POST['notes'], chip_owner=request.user, creation_time=timezone.now())
            new_model.save()
        if process == "Patterning":
            form = PatterningForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            new_model = Patterning(chip_number=request.POST['chip_number'], underlying_material=request.POST['underlying_material'], hdms_prebake_temp=request.POST['hdms_prebake_temp'], hdms_prebake_time=request.POST['hdms_prebake_time'], hdms_spin_rpm=request.POST['hdms_spin_rpm'], hdms_spin_time=request.POST['hdms_spin_time'], hdms_bake_temp=request.POST['hdms_bake_temp'], hdms_bake_time=request.POST['hdms_bake_time'], photoresist_spin_rpm=request.POST['photoresist_spin_rpm'], photoresist_spin_time=request.POST['photoresist_spin_time'], photoresist_bake_temp=request.POST['photoresist_bake_temp'], photoresist_bake_time=request.POST['photoresist_bake_time'], exposure_pattern=request.POST['exposure_pattern'], exposure_time=request.POST['exposure_time'], develop_time=request.POST['develop_time'], metric_pattern_quality=request.POST['metric_pattern_quality'], metric_leftover_photoresist=request.POST['metric_leftover_photoresist'], metric_missing_photoresist=request.POST['metric_missing_photoresist'], metric_contaminants=request.POST['metric_contaminants'], metrology_link=request.POST['metrology_link'], notes=request.POST['notes'], chip_owner=request.user, creation_time=timezone.now())
            new_model.save()
        if process == "Plasma Clean":
            form = PlasmaCleanForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            new_model = PlasmaClean(chip_number=request.POST['chip_number'], o2_flow=request.POST['o2_flow'], rf_power=request.POST['rf_power'], clean_time=request.POST['clean_time'], metric_contaminants=request.POST['metric_contaminants'], metrology_link=request.POST['metrology_link'], notes=request.POST['notes'], chip_owner=request.user, creation_time=timezone.now())
            new_model.save()
        if process == "Plasma Etch":
            form = PlasmaEtchForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            new_model = PlasmaEtch(chip_number=request.POST['chip_number'], o2_flow=request.POST['o2_flow'], sf6_flow=request.POST['sf6_flow'], rf_power=request.POST['rf_power'], etch_time=request.POST['etch_time'], etch_depth=request.POST['etch_depth'], metrology_link=request.POST['metrology_link'], notes=request.POST['notes'], chip_owner=request.user, creation_time=timezone.now())
            new_model.save()
    return "Done"

def parse_forms(used_processes, request):
    invalid_form = False
    forms = []
    for process in used_processes:
        if process == "Aluminum Etch":
            form = AluminumEtchSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                invalid_form = True
            if invalid_form:
                forms.append(form)
        if process == "Aluminum Evaporation":
            form = AluminumEvaporationSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                invalid_form = True
            if invalid_form:
                forms.append(form)
        if process == "Deposition":
            form = DepositionTemplateSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                invalid_form = True
            if invalid_form:
                forms.append(form)
        if process == "Oxide Etch":
            form = OxideEtchSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
        if process == "Patterning":
            form = PatterningSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                invalid_form = True
            if invalid_form:
                forms.append(form)
        if process == "Plasma Clean":
            form = PlasmaCleanSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                invalid_form = True
            if invalid_form:
                forms.append(form)
        if process == "Plasma Etch":
            form = PlasmaEtchSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                invalid_form = True
            if invalid_form:
                forms.append(form)
    if invalid_form:
        return ["Invalid", forms]
    return "Done"

@login_required
def start_page(request):
    context = {"message": "Welcome to the Hacker Fab Database"}
    return render(request, "home.html", context)

@login_required
def search_page(request):
    if request.method == 'GET':
        processes = get_processes()
        context = {"message": "Search Data here", "processes": processes}
        return render(request, "search.html", context)
    status = request.POST["status"]
    if status == "Initial":
        context = compute_search_context(request.POST)
        return render(request, "search.html", context)
    used_processes = request.POST["used_process"]
    parsed = parse_forms(used_processes, request)
    if parsed[0] == "Invalid":
        context = {"message": "Invalid Data Input", "processes": processes, "forms": parsed[1], "used_process": used_processes}
        return render(request, "search.html", context)
    processes = get_processes()
    context = {"message": "Data Searched!","processes": processes}
    return render(request, "search.html", context)

@login_required
def input_page(request):
    if request.method == 'GET':
        processes = get_processes()
        context = {"message": "Input Data here","processes": processes}
        return render(request, "input.html", context)
    status = request.POST["status"]
    if status == "Initial":
        new_process = process_input(request.POST, "Process")
        context = compute_input_context(new_process)
        return render(request, "input.html", context)
    process = request.POST["used_process"]
    saved = save_form([process], request)
    if saved[0] == "Invalid":
        context = {"message": "Invalid Data Input", "processes": processes, "forms": [saved[1]], "used_process": process}
        return render(request, "input.html", context)
    processes = get_processes()
    context = {"message": "Data Submitted!","processes": processes}
    return render(request, "input.html", context)

def process_input(request, word):
    return request[word]

def compute_input_context(process):
    measurements = get_input_meas([process])
    processes = get_processes()
    context = {"processes": processes, "forms": measurements, "used_process": process}
    return context

def process_search(request):
    rel_processes = []
    for key, value in request.lists():
        if key != "status":
            k = key[1:]
            rel_processes.append(k)
    rel_processes = rel_processes[:-1]
    return rel_processes

def compute_search_context(request):
    processes = get_processes()
    rel_processes = process_search(request)
    measurements = get_search_meas(rel_processes)
    context = {"message": "Search Data here", "processes": processes, "forms": measurements, "used_process": rel_processes}
    return context

def login_action(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = LoginForm()
        return render(request, 'login.html', context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = LoginForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'login.html', context)

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
   
    login(request, new_user)
    context['Name'] = f"{request.user.first_name} {request.user.last_name}"
    context = {"message": "Succesful Login! Welcome to the Hacker Fab Database"}
    return render(request, 'home.html', context)

@login_required
def logout_action(request):
    logout(request)
    return redirect(reverse('login'))


def register_action(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = RegisterForm()
        return render(request, 'register.html', context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = RegisterForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'register.html', context)

    # At this point, the form data is valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'], 
                                        password=form.cleaned_data['password'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
    new_user.save()

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

    context['Name'] = f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']}"
    login(request, new_user)
    context = {"message": "Succesful Registration! Welcome to the Hacker Fab Database"}
    return render(request, "home.html", context)