from django.http import HttpResponse
from django.shortcuts import render
import yelp
import requests


from wtfsiw.models import User, Location
import logging
logger = logging.getLogger('MYAPP')


def index(request):
    # Render index.html on a GET request
    if request.method == 'GET':
        return render(request, 'wtfsiw/index.html')
    # Invoke the Yelp API call on a POST request if location auto-detect is enabled
    if request.method == 'POST' and request.POST.get('location-input') == '':
        print request.POST.get('location-input')
        print 'auto-detect'
        latitude = request.POST.get('coords[latitude]')
        longitude = request.POST.get('coords[longitude]')
        print latitude
        print longitude
        #position = [str(latitude), str(longitude)]
        r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s" %(str(latitude), str(longitude)))
        if r:
            address = r.json()['results'][0]['formatted_address']
            search_result = yelp.search('wifi+cafe', address)
            print search_result
            return HttpResponse(search_result)  
        else:
           return 'nothing here'

     # Invoke the Yelp API call on a POST request if location is user-submitted
    if request.method == 'POST' and request.POST.get('location-input') != '':
        submitted_loc = request.POST.get('location-input')
        print submitted_loc
        search_result = yelp.search('cafe', submitted_loc)['businesses']
        print search_result
        return HttpResponse(search_result)
        #return render(request, 'wtfsiw/result.html')
    
def result(request):
    print 'hello'
    loc = request.POST.get('coords[latitude]')
    print loc
    return HttpResponse(loc)



#def index(request):

    #return HttpResponse("Hello, world. You're at the polls index.")

#def results(request):

# def profile(request):
#     template = loader.get_template('templates/index.html')
#     users = User.objects.all()
#     #output = ','.join([u.first_name for p in u])
#     return HttpResponse(users)
