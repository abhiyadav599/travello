from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    #return HttpResponse("<h1>hello world</h1>");
    """dest1 = Destination()
    dest1.name = 'mumbai'
    dest1.desc = 'the city of success'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'hyderabad'
    dest2.desc = 'the city of success'
    dest2.img = 'destination_2.jpg'
    dest2.price = 700
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'delhi'
    dest3.desc = 'the city of success'
    dest3.img = 'destination_3.jpg' 
    dest3.price = 700
    dest3.offer = True

    dest = [dest1, dest2, dest3]"""

    dest = Destination.objects.all()
    return render(request, 'index.html', {'dest' : dest})
