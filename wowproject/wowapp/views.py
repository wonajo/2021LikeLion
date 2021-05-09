from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request, 'wowapp/home.html')

def result(request):
        
        list = ('강연우','박경나','박혜준','장한빛','전수현','안현주','김수현','이민정','노은성','김소은','이연수','황서경','김유진','문다연','김정운','오예림')
        manito = random.sample(list, 1)
        return render(request, 'wowapp/result.html', {'manito':manito})