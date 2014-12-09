from django.http import HttpResponse
from django.shortcuts import render
import yelp


from wtfsiw.models import User, Location
import logging
logger = logging.getLogger('MYAPP')


def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'wtfsiw/index.html', (context))



#def index(request):

    #return HttpResponse("Hello, world. You're at the polls index.")

#def results(request):



# def profile(request):
#     template = loader.get_template('templates/index.html')
#     users = User.objects.all()
#     #output = ','.join([u.first_name for p in u])
#     return HttpResponse(users)
