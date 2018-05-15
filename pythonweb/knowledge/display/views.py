from __future__ import unicode_literals

from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import json
from .models import XCheck,XDisease,XSymptom

from .dao import getdata

# 引入表单类
from .forms import AddForm

# # test=[{'name':'12'},{'attr':'red'}]
#
# def druginfo(request,drug_id):
#     print(drug_id)
#     drug=models.Drug.objects.get(pk=drug_id)
#     return render(request,'info.html',{'drug':drug})
#
# def index(request):
#     drugs=models.Drug.objects.all()
#     for d in drugs:
#         print(d.name)
#     return render(request,'test.html',{'drugs':drugs})
#     # return HttpResponse('Hello！')

def display(request):
    return render(request,'Prof.html')

def symptom(request):
    Symptoms=XDisease.nodes.get(name="妊娠合并白血病")

    # symp=[]
    # for i, s in enumerate(Symptoms):
    #     print(s.name)
    #     if(i<800):
    #         dict={}
    #         dict["source"]="症状"
    #         dict["target"]=s.name
    #         dict["rela"]="治疗"
    #         print(dict)
    #         symp.append(dict)
    return render(request,'info.html',{'symptoms':Symptoms})
    # return render(request, 'info.html', {'symptoms': Symptoms})

# def formpost(request):
#     if request.method=='POST':
#         form=AddForm(request.POST)
#
#         if form.is_valid():
#             a=form.cleaned_data['a']
#             b=form.cleaned_data['b']
#             return HttpResponse(str(int(a)+int(b)))
#     else:
#         form=AddForm()
#     print(form)
#     return render(request, 'form.html', {'form': form})

def formpost(request):
    return render(request,'form.html')

def add(request):
    a=request.GET['a']
    b=request.GET['b']
    a=int(a)
    b=int(b)
    return HttpResponse("")

def look(request):
    a=request.GET['text']
    b=request.GET
    print(a)
    return HttpResponse('yes!')

def testclick(request):
    a = request.GET['data']
    print("kaishidayinl:")
    print(a)

    checkss = XCheck.nodes.get(name="心电图")
    rel = checkss.relatedisease.all()
    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("心电图结点如下：")
    print(checkss.bushiyirenqun)
    print("关系如下：")
    print(rel)
    result=[]
    # result.append(checkss)
    for i,r in enumerate(rel):
        dict = {}
        dict["source"] = "心电图"
        dict["target"] = r.name
        dict["rela"] = "checkTodisease"
        result.append(dict)
    return JsonResponse(result,safe=False)


def looks(request):

    a = request.GET['text']
    type = request.GET['type']
    print(a)
    print(type)
    if(a==""):
        return HttpResponse('no text!')

    results=getdata(a,type)
    print(results)

    if(results=="null"):
        print("查不到呀")
        return HttpResponse('no items!')

    # 用httpResponse可直接传一个字典，不需要压缩啥的，传过去就是字典的格式
    # yong json传，前面可以正常接收并用js处理，后面需要有个safe参数！
    return JsonResponse(results,safe=False)

