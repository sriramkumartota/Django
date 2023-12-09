from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from first_app.models import Topic,webpage,Records

def index(request):
    webpages_list = Records.objects.order_by('date')
    date_dict = {'Records':webpages_list}    
    return render(request, '/index.html',context=webpages_list)