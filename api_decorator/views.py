from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# only GET method
def drink_list(request):

    # get all the drinks
    # serialize them
    # return json
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)

    # In order to allow non-dict objects to be serialized set the safe
    # parameter to False.
    # Return a json response, on endpoint
    # http://127.0.0.1:8000/api_drinks/drinks/
    # return JsonResponse(serializer.data, safe=False)

    # return in dictionary without safe=False:
    return JsonResponse({"drinks": serializer.data})


# GET and POST mathods
@api_view(['GET', 'POST'])
def list_drink(request, format=None):

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        # return JsonResponse({"drinks": serializer.data})
        # return HTML DRF
        return Response(serializer.data)

    if request.method == 'POST':

        # Serializer data = request.data
        serializer = DrinkSerializer(data=request.data)

        # Check if serializer is_valid:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# Drink Detail view update, delete
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
