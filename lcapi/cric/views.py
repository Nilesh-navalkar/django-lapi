from django.shortcuts import render,redirect
from django.contrib import messages
import requests
# Create your views here.
apikey='9d16ea73-0027-4af0-84ef-d661fdcede75'
def current(request):
    u='https://api.cricapi.com/v1/currentMatches?apikey='+apikey+'&offset=0'
    response=requests.get(u).json()
    print(len(response['data']))
    #print(response['data'])
    return render(request,'current.html',{"data":response['data']})

def series(request):
    u='https://api.cricapi.com/v1/series?apikey='+apikey+'&offset=0'
    response=requests.get(u).json()
    print(response)
    return render(request,'series.html',{"data":response['data']})

def players(request):
    url='https://api.cricapi.com/v1/players_info?apikey='+apikey+'&offset=0&id='
    u='https://api.cricapi.com/v1/players?apikey='+apikey+'&offset=0'
    response=requests.get(u).json()
    ret=[]
    #print(type(response['data'][0]))
    for i in response['data']:
        #print(i['id'])
        req=url+str(i['id']) 
        nres=requests.get(req).json()
        ret.append(nres['data'])
    print(ret)
    return render(request,'players.html',{"data":ret})
