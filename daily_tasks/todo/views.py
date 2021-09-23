from django.shortcuts import render
from mongoengine.base.fields import ObjectIdField
from .models.tasks import Task
from .controller.connect_database import database
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from pprint import pprint
from bson import ObjectId, json_util
import json
import jwt
# Create your views here.
# @require_http_methods(['POST'])

@api_view(('POST',))
def add(request):
    data = request.data
    print(data)
    user_info = jwt.decode(data['token'], "secret", algorithms=["HS256"])
    print(user_info['_id']['$oid'])
    if request.method=="POST":
        print("inside methoud POST")
        task_1 = Task(user=user_info['username'], user_id=user_info['_id']['$oid'], task=data['task'], description=data['description'], date_added=datetime.now)
        print(task_1)
        task_1.save()
        return Response({"Status":True, "message": "data saved successfully"})
    else:
        return Response({"Status":True, "message":"enter data"})

@api_view(('DELETE',))
@csrf_exempt
def delete(request):
    print("inside try")
    object_id = ObjectId(str(request.POST["object_id"]))
    print(database)
    if request.method=="DELETE":
        data = database.task.find_one({"_id":ObjectId(str(object_id))})
        pprint(data)
        if data is not None:
            print("deleting database")
            database.task.remove({"_id":ObjectId(str(object_id))}, True)
        return JsonResponse({"Status":True, "message":"Task deleted successfully"})
    return JsonResponse({"Status":True, "message":"Input data."})

@api_view(('PATCH',))
@csrf_exempt
def update(request):
    print(request.method)
    if request.method=="PATCH":
        object_id = str(request.POST['object_id'])
        data = Task.objects(id=object_id)
        print(data)
        Task.objects(id=object_id).update(set__task=request.POST['data'], set__description=request.POST['description'])
        return JsonResponse({"Status":True, "message":"Task updated successfully"})
    return JsonResponse({"Status":True, "message":"Input Correct Data"})

# @api_view(('PUT',))
# @csrf_exempt
# def update2(request):
#     # data = database.task.find_one({"_id":ObjectIdField(object_id)})
#     object_id = str(request.POST['object_id'])
#     Task.objects(id=object_id).update(task=request['data'], description=request['description'])
#     return Response({"Status":True, "message":"Task updated successfully"})


@api_view(('GET',))
@csrf_exempt
def get_task_by_id(request):
    object_id = ObjectId(str(request.POST["object_id"]))
    print(object_id)
    data = database["task"].find_one({"_id":object_id})
    pprint(data)
    return JsonResponse({"status": True, "response": json.loads(json_util.dumps(data))})

@api_view(('GET',))
@csrf_exempt
def get_tasks(request):
    token = request.data['token']
    user = jwt.decode(token, "secret", algorithms=["HS256"])
    if request.method=="GET":
        data = database["task"].find({"user":user['username'], "user_id":user['_id']['$oid']})
        data = [x for x in data]
        return JsonResponse({"status": True, "response": json.loads(json_util.dumps(data))})
    return JsonResponse({"Status":True, "message":"Input data"})
