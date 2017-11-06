from django.shortcuts import render,HttpResponse
from OfflineExam.models import Question,answer
from django.template import Context,loader
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def  home(request):
    Questions=Question.objects.all()
    answers= answer.objects.all()
    dic={"qu":Questions,"aw":answers}
    return render(request,"home.html",dic)
# Create your views here.
