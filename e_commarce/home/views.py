from django.shortcuts import render
from django.http import JsonResponse
from .models import *



def index(request):

    jewellerys=Jewellery.objects.all().order_by('id')[:3]
    jewellerys1=Jewellery.objects.all().order_by('id')[3:]
  
    devices= Device.objects.all().order_by('id')[:3]
    devices1= Device.objects.all().order_by('id')[3:]

    cloths =Cloth.objects.all().order_by('id')[:3]
    cloths1 =Cloth.objects.all().order_by('id')[3:]
               

    context = {
        "cloths":cloths,
        "cloths1":cloths1,
    
        "device":devices,
        "device1":devices1,
        
        "Jewellerys":jewellerys,
        "Jewellerys1":jewellerys1,

        "rangeJ":range(int((len(jewellerys)+len(jewellerys1))/2)),
        "rangeD":range(int((len(devices)+len(devices1))/2)),
        "rangeC":range(int((len(cloths)+len(cloths1))/2))
       
    
    }
    return render(request, 'index.html', context)

