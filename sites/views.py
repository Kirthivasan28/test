from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def index(request):
    kirthi = {'message':'Failed'}
    if request.method =='POST':
        kirthi={'message':'Successfully!!'}
    return JsonResponse(kirthi)