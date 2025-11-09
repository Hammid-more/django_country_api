from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Citizen

@csrf_exempt
def citizen_list(request):
    if request.method == "GET":
        citizens = list(Citizen.objects.values())
        return JsonResponse(citizens, safe=False)
    
    elif request.method == "POST":
        data = json.loads(request.body)
        citizen = Citizen.objects.create(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            age=data.get("age")
        )
        return JsonResponse({"id": citizen.id, "first_name": citizen.first_name}, status=201)

@csrf_exempt
def citizen_detail(request, citizen_id):
    try:
        citizen = Citizen.objects.get(id=citizen_id)
    except Citizen.DoesNotExist:
        return JsonResponse({"error": "Citizen not found"}, status=404)
    
    if request.method == "GET":
        return JsonResponse({"id": citizen.id, "first_name": citizen.first_name, "last_name": citizen.last_name, "age": citizen.age})
    
    elif request.method == "PUT":
        data = json.loads(request.body)
        citizen.first_name = data.get("first_name", citizen.first_name)
        citizen.last_name = data.get("last_name", citizen.last_name)
        citizen.age = data.get("age", citizen.age)
        citizen.save()
        return JsonResponse({"message": "Updated successfully"})
    
    elif request.method == "DELETE":
        citizen.delete()
        return JsonResponse({"message": "Deleted successfully"})
