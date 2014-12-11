from django.http import HttpResponse
from django.shortcuts import render
import yelp
import requests
import json
from django.utils.safestring import mark_safe
import random
# from django.views.decorators.clickjacking import xframe_options_exempt

# User and Location models are not currently used; will need for later features
from wtfsiw.models import User, Location

def index(request):
    # Render index.html on a GET request
    if request.method == 'GET':
        return render(request, 'wtfsiw/index.html')

            
def results(request):
    # Set variables when location is based on browser detection
    if request.POST.get('location-input') is None:
        latitude = request.POST.get('coords[latitude]')
        longitude = request.POST.get('coords[longitude]')
        reverse_geocode = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s" %(str(latitude), str(longitude)))

        user_street_address = reverse_geocode.json()['results'][0]['formatted_address']
        yelp_result = (yelp.search('wifi', user_street_address)['businesses'])
        
    # Set variables when location is based on user input
    if request.POST.get('location-input') is not None:
        user_street_address = request.POST.get('location-input')
        yelp_result = (yelp.search('wifi', user_street_address)['businesses'])

    # Mark_safe used to prevent unicode and HTML conversion
    safe_result = mark_safe(json.dumps(yelp_result))
    
    # Error when yelp_result is empty
    if not yelp_result:
        return HttpResponse('Something went wrong when sending Yelp your address... Try again with a different address?')
    
    #Generate the first random location; subsequent randomization is done in browser
    random_result = yelp_result[random.randrange(len(yelp_result))]
    
    template_data = {
        'name': random_result.get('name'),
        'yelp_results': safe_result,
        'user_address': user_street_address,
        'destination_address': random_result.get('location')['address'][0],
        'city': random_result.get('location')['city']
    }

    return render(request, 'wtfsiw/results.html', template_data)

# Generate template for replacing titleblock and map divs with randomized location data on Results page 

def titleblock_map(request):
    template_data = {
        'name': request.POST.get('random_result[name]'),
        'user_address': request.POST.get('userAddress'),
        'destination_address': request.POST.getlist('random_result[location][address][]')[0],
        'city': request.POST.get('random_result[location][city]')
    }
    print template_data
    return render(request, 'wtfsiw/titleblock_map.html', template_data)

def retry(request):
    return render(request, 'wtfsiw/retry.html')

# Profile view not currently being used
# def profile(request):
#     return HttpResponse('profile data goes here')
