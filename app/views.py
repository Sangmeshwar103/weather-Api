from django.shortcuts import render
import requests
api_key = '026200e2d376ec4aba5ca02862340bfd'
# Create your views here.
def index(request):
    context=None
    if request.method == 'POST':

        city = request.POST.get('city')
        
        data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}').json()
        #print(data)
        main = data["weather"][0]['main']
        description = data["weather"][0]['description']
        temp = data['main']['temp']
        wind = data['wind']['speed']
        name = data["name"]
        print(main,description,temp,wind,name)
        context = {
            'main':main,
            'description':description,
            'temp':temp,
            'wind':wind,
            'name':name,
        }
    return render (request,'index.html',context)