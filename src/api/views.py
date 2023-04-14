from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
import json


def is_valid_types(a, b):
    return (isinstance(a, int) and isinstance(b, int)) or (isinstance(a, float) and isinstance(b, float))


def add_view(request, *args, **kwargs):
    if request.method == 'GET':
        response = dict()
        if request.body:
            a, b = json.loads(request.body).values()
            if is_valid_types(a, b):
                response['answer'] = a + b
            else:
                return JsonResponse({
                    'error': 'Types other than int and float are not allowed!'
                })

        return JsonResponse(response)

    return HttpResponseNotAllowed('Only GET request is allowed!')


def subtract_view(request, *args, **kwargs):
    if request.method == 'GET':
        response = dict()
        if request.body:
            a, b = json.loads(request.body).values()
            if is_valid_types(a, b):
                response['answer'] = a - b
            else:
                return JsonResponse({
                    'error': 'Types other than int and float are not allowed!'
                })

        return JsonResponse(response)

    return HttpResponseNotAllowed('Only GET request is allowed!')


def multiply_view(request, *args, **kwargs):
    if request.method == 'GET':
        response = dict()
        if request.body:
            a, b = json.loads(request.body).values()
            if is_valid_types(a, b):
                response['answer'] = a * b
            else:
                return JsonResponse({
                    'error': 'Types other than int and float are not allowed!'
                })

        return JsonResponse(response)

    return HttpResponseNotAllowed('Only GET request is allowed!')


def divide_view(request, *args, **kwargs):
    if request.method == 'GET':
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

        return JsonResponse(response)

    return HttpResponseNotAllowed('Only GET request is allowed!')