from django.shortcuts import render
import json 
import requests 
def index(request):
    selected_year = request.GET.get('selectedYear')
    url = f'https://brasilapi.com.br/api/feriados/v1/{selected_year}'
    headers ={'Content-Type' : 'application/json'}
    response  = requests.get(url, headers=headers)
    
    if response.status_code == 200:

        feriados = json.loads(response.text)
        return render(request, 'information/index.html', {'feriados': feriados})
    else:
        return render(request, 'information/index.html')