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

from data_management.forms import LoginForm, RegisterForm, ChipListSearchForm, AluminumEtchInputForm, AluminumEvaporationInputForm, ChipListForm, DepositionInputForm, OxideEtchInputForm, PatterningInputForm, PlasmaCleanInputForm, PlasmaEtchInputForm
from data_management.models import AluminumEtch, AluminumEvaporation, ChipList, Deposition, OxideEtch, Patterning, PlasmaClean, PlasmaEtch
from data_management.forms import AluminumEtchSearchForm, AluminumEvaporationSearchForm, DepositionSearchForm, OxideEtchSearchForm, PatterningSearchForm, PlasmaCleanSearchForm, PlasmaEtchSearchForm

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
            form = AluminumEtchInputForm()
        if process == "Aluminum Evaporation":
            form = AluminumEvaporationInputForm()
        if process == "Deposition":
            form = DepositionInputForm()
        if process == "Oxide Etch":
            form = OxideEtchInputForm()
        if process == "Patterning":
            form = PatterningInputForm()
        if process == "Plasma Clean":
            form = PlasmaCleanInputForm()
        if process == "Plasma Etch":
            form = PlasmaEtchInputForm()
        f = {"name": f'{process}', "form": form}
        forms.append(f)
    return forms

def get_search_meas(processes):
    forms = []
    for process in processes:
        if process == "AluminumEtch":
            form = AluminumEtchSearchForm()
        if process == "AluminumEvaporation":
            form = AluminumEvaporationSearchForm()
        if process == "Deposition":
            form = DepositionSearchForm()
        if process == "OxideEtch":
            form = OxideEtchSearchForm()
        if process == "Patterning":
            form = PatterningSearchForm()
        if process == "PlasmaClean":
            form = PlasmaCleanSearchForm()
        if process == "PlasmaEtch":
            form = PlasmaEtchSearchForm()
        if process == "ChipList":
            form = ChipListSearchForm()
        f = {"name": f'{process}', "form": form}
        forms.append(f)
    return forms

def save_form(processes, request):
    for process in processes:
        if process == "Aluminum Etch":
            form = AluminumEtchInputForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            new_model = AluminumEtch(
                chip_number = ChipList.objects.get(chip_number=request.POST["chip_number"]),
                AluminumEtch_temp=request.POST['AluminumEtch_temp'], 
                AluminumEtch_time=request.POST['AluminumEtch_time'], 
                AluminumEtch_stir_rpm=request.POST['AluminumEtch_stir_rpm'], 
                AluminumEtch_metric_alum_etch_depth=request.POST['AluminumEtch_metric_alum_etch_depth'], 
                AluminumEtch_metric_photoresist_peeling=request.POST['AluminumEtch_metric_photoresist_peeling'], 
                AluminumEtch_metric_aluminum_peeling=request.POST['AluminumEtch_metric_aluminum_peeling'], 
                AluminumEtch_metrology_link=request.POST['AluminumEtch_metrology_link'], 
                AluminumEtch_notes=request.POST['AluminumEtch_notes'], 
                chip_owner=request.user, AluminumEtch_step_time=timezone.now()
            )
            new_model.save()
        if process == "Aluminum Evaporation":
            form = AluminumEvaporationInputForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            new_model = AluminumEvaporation(
                chip_number = ChipList.objects.get(chip_number=request.POST["chip_number"]),
                AluminumEvaporation_temp=request.POST['AluminumEvaporation_temp'], 
                AluminumEvaporation_time=request.POST['AluminumEvaporation_time'], 
                AluminumEvaporation_pressure_before_start_seq=request.POST['AluminumEvaporation_pressure_before_start_seq'], 
                AluminumEvaporation_pressure_before_evaporation=request.POST['AluminumEvaporation_pressure_before_evaporation'], 
                AluminumEvaporation_metric_layer_thickness=request.POST['AluminumEvaporation_metric_layer_thickness'], 
                AluminumEvaporation_metric_layer_thick_qcm=request.POST['AluminumEvaporation_metric_layer_thick_qcm'], 
                AluminumEvaporation_metric_deposition_rate=request.POST['AluminumEvaporation_metric_deposition_rate'], 
                AluminumEvaporation_metrology_link=request.POST['AluminumEvaporation_metrology_link'], 
                AluminumEvaporation_notes=request.POST['AluminumEvaporation_notes'], 
                chip_owner=request.user, AluminumEvaporation_step_time=timezone.now()
            )
            new_model.save()
        if process == "Deposition":
            form = DepositionInputForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            new_model = Deposition(
                chip_number = ChipList.objects.get(chip_number=request.POST["chip_number"]),
                Deposition_glass_type=request.POST['Deposition_glass_type'], 
                Deposition_cleaning_step=request.POST['Deposition_cleaning_step'], 
                Deposition_days_glass_at_room_temp=request.POST['Deposition_days_glass_at_room_temp'], 
                Deposition_prebake_temp=request.POST['Deposition_prebake_temp'], 
                Deposition_prebake_time=request.POST['Deposition_prebake_time'], 
                Deposition_amount_drops=request.POST['Deposition_amount_drops'], 
                Deposition_spin_rpm=request.POST['Deposition_spin_rpm'], 
                Deposition_spin_time=request.POST['Deposition_spin_time'], 
                Deposition_bake_temp=request.POST['Deposition_bake_temp'], 
                Deposition_bake_time=request.POST['Deposition_bake_time'], 
                Deposition_humidity=request.POST['Deposition_humidity'], 
                Deposition_metric_layer_thickness=request.POST['Deposition_metric_layer_thickness'], 
                Deposition_metric_cracking=request.POST['Deposition_metric_cracking'], 
                Deposition_metric_particles=request.POST['Deposition_metric_particles'], 
                Deposition_metrology_link=request.POST['Deposition_metrology_link'], 
                Deposition_notes=request.POST['Deposition_notes'], 
                chip_owner=request.user, Deposition_step_time=timezone.now()
            )
            new_model.save()
        if process == "Oxide Etch":
            form = OxideEtchInputForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            new_model = OxideEtch(
                chip_number = ChipList.objects.get(chip_number=request.POST["chip_number"]),
                OxideEtch_max_temp_glass_reached=request.POST['OxideEtch_max_temp_glass_reached'], 
                OxideEtch_time=request.POST['OxideEtch_time'], 
                OxideEtch_temp=request.POST['OxideEtch_temp'], 
                OxideEtch_metric_oxide_etch_depth=request.POST['OxideEtch_metric_oxide_etch_depth'], 
                OxideEtch_metrology_link=request.POST['OxideEtch_metrology_link'], 
                OxideEtch_notes=request.POST['OxideEtch_notes'], 
                chip_owner=request.user, OxideEtch_step_time=timezone.now())
            new_model.save()
        if process == "Patterning":
            form = PatterningInputForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            new_model = Patterning(
                chip_number = ChipList.objects.get(chip_number=request.POST["chip_number"]),
                Patterning_underlying_material=request.POST['Patterning_underlying_material'], 
                Patterning_hdms_prebake_temp=request.POST['Patterning_hdms_prebake_temp'], 
                Patterning_hdms_prebake_time=request.POST['Patterning_hdms_prebake_time'], 
                Patterning_hdms_spin_rpm=request.POST['Patterning_hdms_spin_rpm'], 
                Patterning_hdms_spin_time=request.POST['Patterning_hdms_spin_time'], 
                Patterning_hdms_bake_temp=request.POST['Patterning_hdms_bake_temp'], 
                Patterning_hdms_bake_time=request.POST['Patterning_hdms_bake_time'], 
                Patterning_photoresist_spin_rpm=request.POST['Patterning_photoresist_spin_rpm'], 
                Patterning_photoresist_spin_time=request.POST['Patterning_photoresist_spin_time'], 
                Patterning_photoresist_bake_temp=request.POST['Patterning_photoresist_bake_temp'], 
                Patterning_photoresist_bake_time=request.POST['Patterning_photoresist_bake_time'], 
                Patterning_exposure_pattern=request.POST['Patterning_exposure_pattern'], 
                Patterning_exposure_time=request.POST['Patterning_exposure_time'], 
                Patterning_develop_time=request.POST['Patterning_develop_time'], 
                Patterning_metric_pattern_quality=request.POST['Patterning_metric_pattern_quality'], 
                Patterning_metric_leftover_photoresist=request.POST['Patterning_metric_leftover_photoresist'], 
                Patterning_metric_missing_photoresist=request.POST['Patterning_metric_missing_photoresist'], 
                Patterning_metric_contaminants=request.POST['Patterning_metric_contaminants'], 
                Patterning_metrology_link=request.POST['Patterning_metrology_link'], 
                Patterning_notes=request.POST['Patterning_notes'], 
                chip_owner=request.user, Patterning_step_time=timezone.now()
            )
            new_model.save()
        if process == "Plasma Clean":
            form = PlasmaCleanInputForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            new_model = PlasmaClean(
                chip_number = ChipList.objects.get(chip_number=request.POST["chip_number"]),
                PlasmaClean_o2_flow=request.POST['PlasmaClean_o2_flow'], 
                PlasmaClean_rf_power=request.POST['PlasmaClean_rf_power'], 
                PlasmaClean_clean_time=request.POST['PlasmaClean_clean_time'], 
                PlasmaClean_metric_contaminants=request.POST['PlasmaClean_metric_contaminants'], 
                PlasmaClean_metrology_link=request.POST['PlasmaClean_metrology_link'], 
                PlasmaClean_notes=request.POST['PlasmaClean_notes'], 
                chip_owner=request.user, PlasmaClean_step_time=timezone.now()
            )
            new_model.save()
        if process == "Plasma Etch":
            form = PlasmaEtchInputForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            new_model = PlasmaEtch(
                chip_number = ChipList.objects.get(chip_number=request.POST["chip_number"]),
                PlasmaEtch_o2_flow=request.POST['o2_flow'], 
                PlasmaEtch_sf6_flow=request.POST['sf6_flow'], 
                PlasmaEtch_rf_power=request.POST['rf_power'], 
                PlasmaEtch_etch_time=request.POST['etch_time'], 
                PlasmaEtch_etch_depth=request.POST['etch_depth'], 
                PlasmaEtch_metrology_link=request.POST['metrology_link'], 
                PlasmaEtch_notes=request.POST['notes'], 
                chip_owner=request.user, PlasmaEtch_step_time=timezone.now()
            )
            new_model.save()
    return "Done"

def parse_forms(used_processes, request):
    invalid_form = False
    forms = []
    filters = {}
    used_processes = used_processes.split(",")
    for process in used_processes:
        process = re.sub("[^A-Za-z]","",process)
        if process == "ChipList":
            form = ChipListSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                invalid_form = True
            if invalid_form:
                forms.append(form)
            cleaned_data = form.cleaned_data
            for key, value in cleaned_data.items():
                if value != None:
                    filters[key] = value
        if process == "AluminumEtch":
            form = AluminumEtchSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                invalid_form = True
            if invalid_form:
                forms.append(form)
            cleaned_data = form.cleaned_data
            for key, value in cleaned_data.items():
                if value != None:
                    filters[key] = value
        if process == "AluminumEvaporation":
            form = AluminumEvaporationSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                invalid_form = True
            if invalid_form:
                forms.append(form)
            cleaned_data = form.cleaned_data
            for key, value in cleaned_data.items():
                if value != None:
                    filters[key] = value
        if process == "Deposition":
            form = DepositionSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                invalid_form = True
            if invalid_form:
                forms.append(form)
            cleaned_data = form.cleaned_data
            for key, value in cleaned_data.items():
                if value != None:
                    filters[key] = value
        if process == "OxideEtch":
            form = OxideEtchSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                return ["Invalid", form]
            cleaned_data = form.cleaned_data
            for key, value in cleaned_data.items():
                if value != None:
                    filters[key] = value
        if process == "Patterning":
            form = PatterningSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                invalid_form = True
            if invalid_form:
                forms.append(form)
            cleaned_data = form.cleaned_data
            for key, value in cleaned_data.items():
                if value != None:
                    filters[key] = value
        if process == "PlasmaClean":
            form = PlasmaCleanSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                invalid_form = True
            if invalid_form:
                forms.append(form)
            cleaned_data = form.cleaned_data
            for key, value in cleaned_data.items():
                if value != None:
                    filters[key] = value
        if process == "PlasmaEtch":
            form = PlasmaEtchSearchForm(request.POST, request.FILES)
            if not form.is_valid():
                invalid_form = True
            if invalid_form:
                forms.append(form)
            cleaned_data = form.cleaned_data
            for key, value in cleaned_data.items():
                if value != None:
                    filters[key] = value
    if invalid_form:
        return ["Invalid", forms]
    return [filters]

def filter_form(input_dict):
    input_dict = input_dict[0]
    for i in input_dict.keys():
        return
        

@login_required
def start_page(request):
    context = {"message": "Welcome to the Hacker Fab Database"}
    return render(request, "home.html", context)

@login_required
def chip_page(request):
    context = {}
    if request.method == 'GET':
        return render(request, "chip.html", context)
    
    context["chip_acquired"] = "yes"
    try:
        chip = ChipList.objects.get(chip_number=request.POST["chip_number"]) 
    except:
        chip = ChipList(chip_number=request.POST["chip_number"], creation_time=timezone.now(), chip_owner=request.user)
        chip.save()

    status = request.POST["status"]
    if status == "Initial":
        context['creation_time'] = chip.creation_time
        context['chip_owner'] = chip.chip_owner
        context['chip_number'] = chip.chip_number
        context['form'] = ChipListForm(initial={'notes': chip.notes})
        return render(request, 'chip.html', context)
    
    form = ChipListForm(request.POST, request.FILES)
    if not form.is_valid():
        context = {'form': form}
        return render(request, 'chip.html', context)
    
    chip.notes = form.cleaned_data['notes']
    chip.save()
    context['creation_time'] = chip.creation_time
    context['chip_owner'] = chip.chip_owner
    context['chip_number'] = chip.chip_number
    context['form'] = ChipListForm(initial={'notes': chip.notes})
    return render(request, "chip.html", context)

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
            if " " in k:
                k = k.split(" ")[0] + k.split(" ")[1]
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