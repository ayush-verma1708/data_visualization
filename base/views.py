# views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DataEntry2
from django.shortcuts import render


@csrf_exempt
def getData(request):
    if request.method == "POST":
        # Specify the path to your JSON file
        json_file_path = 'static/base/data.json'
        try:
            with open(json_file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
        except FileNotFoundError:
            return JsonResponse({"status": "error", "message": "JSON file not found"})

        # Create DataEntry2 instances from JSON data
        for entry_data in json_data:
            # List of all fields in DataEntry2
            fields = ['intensity', 'sector', 'topic', 'insight', 'url', 'region', 'start_year', 'end_year', 'impact', 'added', 'published', 'country', 'relevance', 'pestle', 'source', 'title', 'likelihood']

            # Check if all fields are present in the dictionary
            if all(field in entry_data for field in fields):
                start_year = entry_data.get('start_year')
                end_year = entry_data.get('end_year')

                # Ensure both start_year and end_year are integers
                try:
                    start_year = int(start_year) if start_year else None
                    end_year = int(end_year) if end_year else None
                except ValueError:
                    start_year = None
                    end_year = None

                DataEntry2.objects.create(
                    intensity=entry_data.get('intensity'),
                    sector=entry_data.get('sector'),
                    topic=entry_data.get('topic'),
                    insight=entry_data.get('insight'),
                    url=entry_data.get('url'),
                    region=entry_data.get('region'),
                    start_year=start_year,
                    end_year=end_year,
                    impact=entry_data.get('impact'),
                    added=entry_data.get('added'),
                    published=entry_data.get('published'),
                    country=entry_data.get('country'),
                    relevance=entry_data.get('relevance'),
                    pestle=entry_data.get('pestle'),
                    source=entry_data.get('source'),
                    title=entry_data.get('title'),
                    likelihood=entry_data.get('likelihood')
                )

        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method. Use POST."})


@csrf_exempt
def deleteAllData(request):
    if request.method == "POST":
        try:
            # Delete all data from the DataEntry2 model
            DataEntry2.objects.all().delete()
            return JsonResponse({"status": "success", "message": "All data deleted successfully."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Error deleting data: {str(e)}"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method. Use POST."})
    
def homepage(request):
    DataEntry_info = DataEntry2.objects.all()
    context = {'Data': DataEntry_info}
    return render(request,'homepage.html',context)

def get_data_api(request):
    data_entries = DataEntry2.objects.all()
    data_list = []
    for entry in data_entries:
        data_list.append({
            'end_year': entry.end_year,
            'intensity': entry.intensity,
           'topic': entry.topic,
           'region': entry.region,
           'start_year': entry.start_year,
           'country': entry.country,
           'relevance': entry.relevance,
           'likelihood': entry.likelihood,
        })
    return JsonResponse({'data': data_list})

def dashboard_view(request):
    return render(request, 'dashboard.html')


@csrf_exempt
def filter_Data(request):
    if request.method == "POST":
        try:
            # Retrieve filter parameters from the request
            start_year = request.POST.get('start_year')
            end_year = request.POST.get('end_year')

            # Query the database with the specified filters
            filtered_data = DataEntry2.objects.filter(
                start_year=start_year,
                end_year=end_year
            )

            # Convert the queryset to a list of dictionaries
            filtered_data_list = list(filtered_data.values())

            return JsonResponse({"status": "success", "data": filtered_data_list})
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Error filtering data: {str(e)}"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method. Use POST."})