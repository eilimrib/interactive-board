from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from board.serializers.card_serializer import CardSerializer
from board.models.card_model import Card
from rest_framework.parsers import JSONParser
# Create your views here.


@csrf_exempt
def cards(request):
    '''
    List all card snippets
    '''
    if(request.method == 'GET'):
        # get all the cards
        cards = Card.objects.all()
        # serialize the card data
        serializer = CardSerializer(cards, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = CardSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def card_detail(request, pk):
    try:
        # obtain the card with the passed id.
        card = Card.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = CardSerializer(cards, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the card
        card.delete() 
        # return a no content response.
        return HttpResponse(status=204) 