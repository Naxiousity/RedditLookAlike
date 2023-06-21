from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRoutes(request): #Remember that this is REST Framework - allows users to get our data if they want to
    routes =[
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return JsonResponse(routes, safe=False) #safe=False means that we can use more than Python dictionaries in the resonse (routes); makes the list into a Json list/data 