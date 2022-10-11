from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from board.serializers.list_serializer import ListSerializer
from board.models.list_model import List
from rest_framework.parsers import JSONParser
# Create your views here.


@csrf_exempt
def lists(request):
    '''
    List all list snippets
    '''
    if(request.method == 'GET'):
        # get all the lists
        lists = List.objects.all()
        # serialize the list data
        serializer = ListSerializer(lists, many=True, context={"request": request})
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = ListSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def list_detail(request, pk):
    try:
        # obtain the list with the passed id.
        list = List.objects.get(pk=pk)
    except Exception as e:
        print(e)
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'GET'):
        serializer = ListSerializer(list, many=False)
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = ListSerializer(list, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the list
        list.delete() 
        # return a no content response.
        return HttpResponse(status=204) 