from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Citizen
import json

# List all citizens or create a new one
@csrf_exempt
def citizen_list(request):
    if request.method == 'GET':
        citizens = list(Citizen.objects.values(
            'id', 'first_name', 'father_name', 'mother_name', 'home_town', 'gender'
        ))
        return JsonResponse(citizens, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        citizen = Citizen.objects.create(
            first_name=data.get('first_name'),
            father_name=data.get('father_name'),
            mother_name=data.get('mother_name'),
            home_town=data.get('home_town'),
            gender=data.get('gender')
        )
        return JsonResponse({
            "message": "Citizen added",
            "citizen": {
                "id": citizen.id,
                "first_name": citizen.first_name,
                "father_name": citizen.father_name,
                "mother_name": citizen.mother_name,
                "home_town": citizen.home_town,
                "gender": citizen.gender
            }
        })

# Get, update, or delete a single citizen
@csrf_exempt
def citizen_detail(request, id):
    try:
        citizen = Citizen.objects.get(id=id)
    except Citizen.DoesNotExist:
        return JsonResponse({"error": "Citizen not found"}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            "id": citizen.id,
            "first_name": citizen.first_name,
            "father_name": citizen.father_name,
            "mother_name": citizen.mother_name,
            "home_town": citizen.home_town,
            "gender": citizen.gender
        })

    elif request.method in ['PUT', 'PATCH']:
        data = json.loads(request.body)
        citizen.first_name = data.get('first_name', citizen.first_name)
        citizen.father_name = data.get('father_name', citizen.father_name)
        citizen.mother_name = data.get('mother_name', citizen.mother_name)
        citizen.home_town = data.get('home_town', citizen.home_town)
        citizen.gender = data.get('gender', citizen.gender)
        citizen.save()
        return JsonResponse({
            "message": "Citizen updated",
            "citizen": {
                "id": citizen.id,
                "first_name": citizen.first_name,
                "father_name": citizen.father_name,
                "mother_name": citizen.mother_name,
                "home_town": citizen.home_town,
                "gender": citizen.gender
            }
        })

    elif request.method == 'DELETE':
        citizen.delete()
        return JsonResponse({"message": "Citizen deleted"})
