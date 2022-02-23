from django.shortcuts import render, HttpResponse
import datetime
import requests
import json
import collections, functools, operator
# Create your views here.
def index(request):

    context = {
        
    }
    return render(request, "index.html", context)

def about(request):

    current_date = datetime.datetime.now()
    years_experience = current_date.year-2011

    #git = requests.get('https://api.github.com/users/mhw29').json()

    #repos = requests.get('https://api.github.com/users/mhw29/repos').json()
    
    languages = []
    #for repo in repos:
        #languages.append(requests.get(f'https://api.github.com/repos/mhw29/{repo["name"]}/languages').json())

    #result = dict(functools.reduce(operator.add,map(collections.Counter, languages)))
    result = {'Ruby': 16.75535696706518, 'HTML': 22.720121486569756, 'CSS': 39.97826950913155, 'JavaScript': 2.4125949341704676, 'CoffeeScript': 0.12487740138331345, 'Python': 0.5986823155369364, 'Dockerfile': 0.14447494977558528, 'Shell': 0.028256930240019833, 'OpenSCAD': 13.58265060943818, 'C++': 3.6547148966890166}
    #total_bytes = sum(result.values())

    #for k in result.keys():
    #    result[k] = (result[k]/total_bytes)*100

    context = {
        'years_of_experience' : years_experience,
        #'projects_worked' : git['public_repos'],
        'projects_worked' : 10,
        'languages' : result
    }
    return render(request,"about.html", context)