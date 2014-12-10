from django.http import HttpResponse
from django.shortcuts import render
import yelp
import requests


from wtfsiw.models import User, Location
# import logging
# logger = logging.getLogger('MYAPP')


def index(request):
    # Render index.html on a GET request
    if request.method == 'GET':
        return render(request, 'wtfsiw/index.html')
    # Invoke Yelp API based on auto-detected location
    if request.method == 'POST' and request.POST.get('location-input') is None:
        # print 'auto-detect'
        latitude = request.POST.get('coords[latitude]')
        longitude = request.POST.get('coords[longitude]')
        r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s" %(str(latitude), str(longitude)))
        if r:
            address = r.json()['results'][0]['formatted_address']
            search_result = yelp.search('internet', address)['businesses']
            # return the data to complete the AJAX call, and invoke a GET request for the Result page
            return HttpResponse(search_result)


        else:
            return 'nothing here'

     # Invoke Yelp API on user-submitted location
    if request.method == 'POST' and request.POST.get('location-input') is not None:
        submitted_loc = request.POST.get('location-input')
        # print submitted_loc
        search_result = yelp.search('internet', submitted_loc)['businesses']
        # print search_result
        return HttpResponse(search_result)
        #return render(request, 'wtfsiw/result.html')
    
def result(request):
    print 'result path'
    print request
    return render(request, 'wtfsiw/results.html', {'test':'hello'})

def profile(request):
    return HttpResponse('profile goes here')

#def index(request):

    #return HttpResponse("Hello, world. You're at the polls index.")

#def results(request):

# def profile(request):
#     template = loader.get_template('templates/index.html')
#     users = User.objects.all()
#     #output = ','.join([u.first_name for p in u])
#     return HttpResponse(users)
