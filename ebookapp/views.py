from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
import jwt

# Create your views here.

@api_view(['GET','POST','PUT'])
def funapi(request, id=0):
    #to post in api
    if request.method =="POST":
        data=request.data

        userId = data['userId']
        userObj = User.objects.get(id=userId)

        savedata=Ebook(title=data['title'],author=data['author'],genre=data['genre'],review=data['review'],favourite=data['favourite'], fkUser=userObj)
        savedata.save()
        return Response("data inserted")

    # get in api
    elif request.method == "GET":
        # get through params
        params = request.GET
        obj1 = Ebook.objects.filter(fkUser=params['userId'])

        jsonData = [{'id':i.id,'title':i.title,'author':i.author,'genre':i.genre,'review':i.review,'favourite':i.favourite}for i in obj1]

        jsonData = sorted(jsonData, key=lambda d: d['title'])

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
    return Response('delete successfully')

# to register user
@api_view(['POST'])
def funuserreg(request):
    if request.method == "POST":
        data = request.data
        sd = User(username=data['username'],password=data['password']) 
        sd.save() 
        return Response('User registered successfully')

# to login user
@api_view(['POST'])
def funuserlogin(request):
    if request.method == "POST":        
       data = request.data
       username=data['username']
       password = data['password']
       lg=User.objects.get(username=username)
       if lg.password==password:
           # to covert into jwt token
            encoded_jwt = jwt.encode({"userid": lg.id}, "django-insecure-2a*#0#4&-3e+xup807gm(kvs(c%xnsh0_3fu8y3-7#xpkjg0-2", algorithm="HS256")
            obj3=Usertoken(token=encoded_jwt, fkUser=lg)
            obj3.save()
            return Response('User login successfully')
       else:
           return Response('Login Failed')     

# to get user details in user table
@api_view(['GET'])            
def funuserget(request):
    if request.method == "GET":
        obj1=User.objects.all()
        jsonData=[{'id':i.id,'username':i.username,'password':i.password}for i in obj1]
        return Response({'data':jsonData})

