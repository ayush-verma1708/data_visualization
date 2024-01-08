# views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DataEntry

@csrf_exempt
def getData(request):
    if request.method == "POST":
        # Specify the path to your JSON file
        json_file_path = 'base/static/base/data.json'

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
