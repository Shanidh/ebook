from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','POST','PUT'])
def funapi(request, id=0):
    #to post in api
    if request.method =="POST":
        data=request.data
        savedata=Ebook(title=data['title'],author=data['author'],genre=data['genre'],review=data['review'],favourite=data['favourite'])
        savedata.save()
        return Response("data inserted")
    # get in api
    elif request.method == "GET":
        obj1=Ebook.objects.all()
        jsonData=[{'id':i.id,'title':i.title,'author':i.author,'genre':i.genre,'review':i.review,'favourite':i.favourite}for i in obj1]
        return Response({'data':jsonData})  
    # update in api
    elif request.method == "PUT":   
        data=request.data
        Ebook.objects.filter(id=data['id']).update(title=data['title'],author=data['author'],genre=data['genre'],review=data['review'],favourite=data['favourite'])
        return Response('update successful')    

        
#to delete in api
@api_view(['DELETE'])
def fundeleteapi(request,delid):
    Ebook.objects.filter(id=delid).delete()    
    return Response('delete successful')

@api_view(['FILTER'])    
def funfilter(request):
    Ebook.objects.filter(genre="dsfsdf")

       