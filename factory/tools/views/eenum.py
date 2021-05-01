# coding: utf-8
from enum import Enum
from django.http import HttpResponse, JsonResponse


class Region(Enum):
    上海 = 1
    北京 = 2
    长沙 = 3


class Type(Enum):
    美食餐厅线上活动 = 1
    地推活动 = 2
    线下主题活动 = 3
    单纯品牌曝光 = 4


class Resource(Enum):
    线上品牌商赞助 = 1
    线下场地免费 = 2


def get_region(request):
    info = []
    for r in Region:
        info.append({'value': r.value, 'label': r.name})
    response = {"returnCode": 0, "returnInfo": info}
    return JsonResponse(response, content_type='application/json;charset=utf-8', safe=False)


def get_type(request):
    info = []
    for r in Type:
        info.append({'value': r.value, 'label': r.name})
    response = {"returnCode": 0, "returnInfo": info}
    return JsonResponse(response, content_type='application/json;charset=utf-8', safe=False)


def get_resource(request):
    info = []
    for r in Resource:
        info.append({'value': r.value, 'label': r.name})
    response = {"returnCode": 0, "returnInfo": info}
    return JsonResponse(response, content_type='application/json;charset=utf-8', safe=False)
