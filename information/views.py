from django.shortcuts import render
import json 
import requests 
from datetime import datetime

def index(request):
    selected_year = request.GET.get('selectedYear')
    url = f'https://brasilapi.com.br/api/feriados/v1/{selected_year}'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        feriados = []
        data = json.loads(response.text)
        
        for feriado in data:
            feriado['date'] = datetime.strptime(feriado['date'], '%Y-%m-%d').strftime('%A, %d ,%B ,%Y')
            feriados.append(feriado)
            
        return render(request, 'information/index.html', {'feriados': feriados})
    else:
        return render(request, 'information/index.html')
