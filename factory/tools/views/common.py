# coding: utf-8

from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from faker import Faker
import time, json, datetime
from factory.models import Promotion
from factory.tools.views.eenum import Region, Resource, Type


def get_idcards(request):
    num = request.GET.get("num", 1)
    num = int(num)
    faker = Faker('zh_CN')
    name = faker.name()
    phone = faker.phone_number()
    id = faker.ssn(min_age=18, max_age=90)
    adderss = faker.address()
    idcard = {'name': name, 'phone': phone, 'id': id, 'address': adderss}
    time.sleep(1)
    response = {"returnCode": 0, "returnInfo": idcard}
    return JsonResponse(response, content_type='application/json;charset=utf-8', safe=False)


def addPromotion(request):
    # print(request.content_type)
    if request.method == 'POST' and request.content_type == 'application/x-www-form-urlencoded':
        name = request.POST.get('name')
        region = request.POST.get('region', 0)
        delivery = request.POST.get('delivery', 0)
        resource = request.POST.get('resource', 0)
        desc = request.POST.get('desc', '')
        if delivery == 'true':
            delivery = True
        else:
            delivery = False
        # print(name, region, delivery, resource, desc)
        promotion = Promotion()
        try:
            promotion.insert(name=name, region=region, delivery=delivery, resource=resource, desc=desc)
            response = {"returnCode": 0, "returnInfo": '提交成功', 'returnData': {}}
        except Exception:
            response = {"returnCode": -1, "returnInfo": '数据入库失败', 'returnData': {}}
        time.sleep(1)
        return JsonResponse(response, content_type='application/json;charset=utf-8', safe=False)
    elif request.method == 'POST' and request.content_type == 'application/json':
        body = json.loads(request.body)
        print(body)
        if body['start_time']:
            start_time = datetime.datetime.strptime(body['start_time'], '%Y-%m-%dT%H:%M:%S.000Z') + datetime.timedelta(
                hours=8)
            body['start_time'] = start_time
        else:
            del body['start_time']
        if body['end_time']:
            end_time = datetime.datetime.strptime(body['end_time'], '%Y-%m-%dT%H:%M:%S.000Z') + datetime.timedelta(
                hours=8)
            body['end_time'] = end_time
        else:
            del body['end_time']
        print(body)
        try:
            promotion = Promotion()
            promotion.insert(**body)
            response = {"returnCode": 0, "returnInfo": '提交成功', 'returnData': {}}
        except Exception:
            response = {"returnCode": -1, "returnInfo": '数据入库失败', 'returnData': {}}
        time.sleep(1)
        return JsonResponse(response, content_type='application/json;charset=utf-8', safe=False)
    else:
        response = {"returnCode": -1, "returnInfo": '请求类型错误', 'returnData': {}}
        return JsonResponse(response, content_type='application/json;charset=utf-8', safe=False)


def getPromotion(request):
    page = request.GET.get('page',1)
    page = int(page)
    promtions = Promotion.objects.all().order_by('create_time')
    count = promtions.count()
    paginator = Paginator(promtions, 10)  # 设置每页数据10条
    total_page = paginator.num_pages
    page1 = paginator.page(page)
    page_data = list(page1.object_list.values())
    print(page_data)
    for i in page_data:
        for j in i:
            if isinstance(i[j], datetime.datetime):
                i[j] = i[j].strftime('%Y-%m-%d %H:%M:%S')
            if j == 'region' and i[j] != 0:
                i[j] = Region(i[j]).name
            if j == 'type':
                l = eval(i[j])
                ll = ''
                for m in l:
                    ll = ll + Type(m).name + ','
                i[j] = ll
            if j == 'resource' and i[j] != 0:
                i[j] = Resource(i[j]).name
    response = {"returnCode": 0, "returnInfo": '获取数据成功', "renturnData": page_data}
    print(response)

    response = {"returnCode": 0, "returnInfo": '获取数据成功',
                "renturnData": {"total_page": total_page, "current_page": page, "count": count,
                                'data': page_data}}

    return JsonResponse(response, content_type='application/json;charset=utf-8', safe=False)
