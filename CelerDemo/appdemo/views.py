from django.shortcuts import render,HttpResponse
from appdemo.tasks import add
from celery.result import AsyncResult

# Create your views here.

def celery_test(request):
    task = add.delay(65,24)
    res = AsyncResult(task.id)
    print(res.ready())
    print(res.status)
    return HttpResponse(task.id)
