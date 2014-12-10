from django.http import HttpResponse
from django.shortcuts import render
import yelp
import requests
import json
from django.utils.safestring import mark_safe
import random

from wtfsiw.models import User, Location
# import logging
# logger = logging.getLogger('MYAPP')

def index(request):
    # Render index.html on a GET request
    if request.method == 'GET':
        return render(request, 'wtfsiw/index.html')
    # Flow for auto-detected location
    if request.method == 'POST' and request.POST.get('location-input') is None:
        latitude = request.POST.get('coords[latitude]')
        longitude = request.POST.get('coords[longitude]')
        r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s" %(str(latitude), str(longitude)))
        if r:
            address = r.json()['results'][0]['formatted_address']
            search_result = json.dumps(yelp.search('internet', address)['businesses'])
            # return the data to complete the AJAX call, and invoke a GET request for the Result page
            return HttpResponse(search_result)
        else:
            return 'nothing here'

     # Flow for user-submitted location
    if request.method == 'POST' and request.POST.get('location-input') is not None:
        submitted_loc = request.POST.get('location-input')
        # mark_safe used to prevent unicode and HTML conversion
        yelp_result = (yelp.search('internet', submitted_loc)['businesses'])
        safe_result = mark_safe(json.dumps(yelp_result))
        random_result = yelp_result[random.randrange(len(yelp_result))]
        template_data = {
          'name': random_result.get('name'),
          'test': 'test user',
          'yelpResults': safe_result
        }

        return render(request, 'wtfsiw/results.html', template_data)
        #return render(request, 'wtfsiw/result.html')
    
def results(request):
    print request.GET.get('name')
    template_data = {
      'name': request.GET.get('name')
    }
    return render(request, 'wtfsiw/results.html', template_data)

def profile(request):
    return HttpResponse('profile data goes here')
