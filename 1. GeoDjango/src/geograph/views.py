from django.shortcuts import render
# from django.views.generic import ListView
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import Agent
from geopy.geocoders import Nominatim
from formtools.wizard.views import SessionWizardView
from django.shortcuts import redirect
from .forms import step1, step2



def User_Adress(request):
    adress = "Adresss" # Use DJANGO_FORM . Under construction
    geolocator = Nominatim(user_agent="nominatum")
    location = geolocator.geocode(adress)
    user_location = Point(location.longitude, location.latitude, srid=4326)

    queryset = Agent.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    context = {
        'adress': location,
        'object_list': queryset
    }
    return render(request, 'test.html', context) 
    

def Home(request):
    return render(request, 'index.html', {}) 
s

class PriceWizard(SessionWizardView):
    template_name = "page1.html"
    form_list = [step1, step2]

    def done(self, form_list, **kwargs):
        return render(self.request, 'final.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })