from django.shortcuts import render

def home(request):
    import requests
    import json

    # pk_08c7a6a3676c470d899103c8e2ed5602
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_08c7a6a3676c470d899103c8e2ed5602")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})