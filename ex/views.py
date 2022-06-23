from django.http import JsonResponse
from django.shortcuts import render


def ajax(request):
    return render(request, 'ajax.html')

def func1(request):
    json_data = {
        'message':'안녕하세요',
        '배울 과목' : ['파이썬', '장고', '리액트', 'k8s']
    }
    return JsonResponse(json_data)