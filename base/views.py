# views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DataEntry
from django.shortcuts import render


@csrf_exempt
def getData(request):
    if request.method == "POST":
        # Specify the path to your JSON file
        json_file_path = 'static/base/data.json'
        try:
            with open(json_file_path, 'r') as file:
                json_data = json.load(file)
        except FileNotFoundError:
            return JsonResponse({"status": "error", "message": "JSON file not found"})

        # Create DataEntry instances from JSON data
        for entry in json_data:
            DataEntry.objects.create(
                intensity=entry.get('intensity'),
                likelihood=entry.get('likelihood'),
                relevance=entry.get('relevance'),
                year=entry.get('year'),
                country=entry.get('country'),
                topics=entry.get('topics'),
                region = entry.get('region'),
                city=entry.get('city'),
            )

        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method. Use POST."})

def homepage(request):
    DataEntry_info = DataEntry.objects.all()
    context = {'Data': DataEntry_info}
    return render(request,'homepage.html',context)

def get_data_api(request):
    data_entries = DataEntry.objects.all()
    data_list = []
    for entry in data_entries:
        data_list.append({
            'intensity': entry.intensity,
            'likelihood': entry.likelihood,
            'relevance': entry.relevance,
            'year': entry.year,
            'country': entry.country,
            'topics': entry.topics,
            'region': entry.region,
            'city': entry.city,
        })
    return JsonResponse({'data': data_list})

def dashboard_view(request):
    return render(request, 'dashboard.html')