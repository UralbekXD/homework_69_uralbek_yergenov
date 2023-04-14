from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
import json


def is_valid_types(a, b):
    return (isinstance(a, int) and isinstance(b, int)) or (isinstance(a, float) and isinstance(b, float))


def add_view(request, *args, **kwargs):
    if request.method == 'POST':
        response = dict()
        if request.body:
            a, b = json.loads(request.body).values()
            print(a, b)
            if is_valid_types(a, b):
                response['answer'] = a + b
            else:
                return JsonResponse({
                    'error': 'Types other than int and float are not allowed!'
                })
        else:
            return JsonResponse({'error': 'No data sent'})

        return JsonResponse(response)

    return HttpResponseNotAllowed('Only POST request is allowed!')


def subtract_view(request, *args, **kwargs):
    if request.method == 'POST':
        response = dict()
        if request.body:
            a, b = json.loads(request.body).values()
            if is_valid_types(a, b):
                response['answer'] = a - b
            else:
                return JsonResponse({
                    'error': 'Types other than int and float are not allowed!'
                })
        else:
            return JsonResponse({'error': 'No data sent'})

        return JsonResponse(response)

    return HttpResponseNotAllowed('Only POST request is allowed!')


def multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        response = dict()
        if request.body:
            a, b = json.loads(request.body).values()
            if is_valid_types(a, b):
                response['answer'] = a * b
            else:
                return JsonResponse({
                    'error': 'Types other than int and float are not allowed!'
                })
        else:
            return JsonResponse({'error': 'No data sent'})

        return JsonResponse(response)

    return HttpResponseNotAllowed('Only POST request is allowed!')


def divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        response = dict()
        if request.body:
            a, b = json.loads(request.body).values()
            if is_valid_types(a, b):
                try:
                    response['answer'] = a / b
                except ZeroDivisionError:
                    return JsonResponse({
                        'error': 'Division by zero!'
                    })
            else:
                return JsonResponse({
                    'error': 'Types other than int and float are not allowed!'
                })
        else:
            return JsonResponse({'error': 'No data sent'})

        return JsonResponse(response)

    return HttpResponseNotAllowed('Only POST request is allowed!')