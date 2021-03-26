from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .models import Vaccine
from .forms import VaccineRegister, VaccineBrowse

# Create your views here.
def main(request):
    return render(request, 'clinica/main.html')

def register(request):
    if request.method == 'POST':
        vaccine_register_form = VaccineRegister(request.POST, request.FILES)
        if vaccine_register_form.is_valid():
            input_data = request.POST.copy()
            new_vaccine_entry = Vaccine()
            new_vaccine_entry.short_description = input_data.get('short_description_field')
            new_vaccine_entry.long_description = input_data.get('long_description_field')
            new_vaccine_entry.quantity = input_data.get('quantity_field')
            new_vaccine_entry.unit_price = input_data.get('unit_price_field')
            new_vaccine_entry.save()
            messages.success(request, 'Vacinas registradas com sucesso.');
        else:
            messages.error(request, 'Formulário incompleto.')
    else:
        vaccine_register_form = VaccineRegister()

    return render(request, 'clinica/register.html', {
        'form': vaccine_register_form
    })

def browse(request):
    if request.method == 'POST':
        vaccine_browse_form = VaccineBrowse(request.POST, request.FILES)
        input_data = request.POST.copy()
        vaccine_database = Vaccine.objects.all()

        if input_data.get('filter_short_description_field') != '':
            vaccine_database = vaccine_database.filter(short_description__icontains=input_data.get('filter_short_description_field'))

        if input_data.get('filter_long_description_field') != '':
            vaccine_database = vaccine_database.filter(long_description__icontains=input_data.get('filter_long_description_field'))

        if input_data.get('filter_min_quantity_field') != '':
            filter = input_data.get('filter_min_quantity_field')
            if filter.isnumeric():
                filter = int(filter)
                vaccine_database = vaccine_database.filter(quantity__gte=filter)

        if input_data.get('filter_max_quantity_field') != '':
            filter = input_data.get('filter_max_quantity_field')
            if filter.isnumeric():
                filter = int(filter)
                vaccine_database = vaccine_database.filter(quantity__lte=filter)

        if input_data.get('filter_min_unit_price_field') != '':
            filter = input_data.get('filter_min_unit_price_field')
            try:
                float(filter)
                filter = float(filter)
                vaccine_database = vaccine_database.filter(unit_price__gte=filter)
            except ValueError:
                pass

        if input_data.get('filter_max_unit_price_field') != '':
            filter = input_data.get('filter_max_unit_price_field')
            try:
                float(filter)
                filter = float(filter)
                vaccine_database = vaccine_database.filter(unit_price__lte=filter)
            except ValueError:
                pass

    else:
        vaccine_browse_form = VaccineBrowse()
        vaccine_database = Vaccine.objects.all()

    return render(request, 'clinica/browse.html', {
        'form': vaccine_browse_form,
        'vaccine_database': vaccine_database
    })

def buy(request):
    return render(request, 'clinica/buy.html')
