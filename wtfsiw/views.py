from django.http import HttpResponse
from django.shortcuts import render
import yelp
import requests
import json
from django.utils.safestring import mark_safe
import random
#from django.views.decorators.clickjacking import xframe_options_exempt


from wtfsiw.models import User, Location
# import logging
# logger = logging.getLogger('MYAPP')

def index(request):
    # Render index.html on a GET request
    if request.method == 'GET':
        return render(request, 'wtfsiw/index.html')

    # Flow for auto-detected location
    # note that the user's location is passed to the browser, which then passes the address back to the server to populate the context for the Result template (to save in localStorage when the templte is rendered)
    if request.method == 'POST' and request.POST.get('location-input') is None:
        latitude = request.POST.get('coords[latitude]')
        longitude = request.POST.get('coords[longitude]')
        r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s" %(str(latitude), str(longitude)))

        address = r.json()['results'][0]['formatted_address']
        search_result = json.dumps((yelp.search('wifi', address)['businesses']))
        # return the data to complete the AJAX call, and invoke a GET request for the Result page
        package = json.dumps([address, search_result])
        return HttpResponse(package)


     # Flow for user-submitted location
    if request.method == 'POST' and request.POST.get('location-input') is not None:
        submitted_loc = request.POST.get('location-input')
        yelp_result = (yelp.search('wifi', submitted_loc)['businesses'])
        if yelp_result: 
            # mark_safe used to prevent unicode and HTML conversion
            safe_result = mark_safe(json.dumps(yelp_result))
            random_result = yelp_result[random.randrange(len(yelp_result))]
            template_data = {
                'name': random_result.get('name'),
                'yelp_results': safe_result,
                'user_address': submitted_loc,
                'destination_address': random_result.get('location')['address'][0],
                'city': random_result.get('location')['city']
            }
            # return render(request, 'wtfsiw/results.html', template_data)
            return 'ok'
            self.results(request)
        else:
            return HttpResponse("null")

            
def results(request):
    template_data = {
      'name': request.GET.get('randomLoc[name]'),
      'destination_address': request.GET.getlist('randomLoc[location][address][]')[0],
      'city': request.GET.get('randomLoc[location][city]'),
      'user_address': request.GET.get('userAddress')
    }
    return render(request, 'wtfsiw/results.html', template_data)

def retry(request):
    return render(request, 'wtfsiw/retry.html')

def profile(request):
    return HttpResponse('profile data goes here')
