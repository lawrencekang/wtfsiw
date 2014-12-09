from django.http import HttpResponse
from django.shortcuts import render
import yelp


from wtfsiw.models import User, Location
import logging
logger = logging.getLogger('MYAPP')


def index(request):
    if request.GET
      return render(request, 'wtfsiw/index.html')
    if request.POST
      print 'hello'
      loc = request.POST.get('coords[latitude]')
      print loc
      return HttpResponse(loc)


def query(request):
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
