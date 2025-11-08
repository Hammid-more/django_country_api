from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def citizen_list(request):
    try:
        return Response({"message": "List of citizens endpoint is working!"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
