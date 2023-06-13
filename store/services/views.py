from django.shortcuts import render
# from ..models import ItemGs25, ItemCu
from . import gs_crawl
from ..database.gs_repository import saveCrawlData, selectAllGS, deleteAllDatas
from django.http import HttpResponse
import json


def hello(request):
    return render(request, 'hello/hello.html', {})

# 이벤트 크롤링 수동 버튼
def crawlEvent(request):
    # gsDatas = crawl.getScrapGSDatas()
    # print('gsDatas : ', gsDatas)
    return render(request, 'store/load-event.html',{})

# 제로필 생성
def generate_next_number(current_number):
    number = int(current_number)
    next_number = number + 1
    next_number_str = str(next_number).zfill(len(current_number))
    return next_number_str


# 이벤트 저장
def saveEvent(request, name):
    print('request :: ', request)
    print('name :: ', name)

    deleteAllDatas()

    gsDatas = gs_crawl.getScrapGSDatas()
    current_number = "00000"

    for i in gsDatas:
        current_number = generate_next_number(current_number)
        saveCrawlData( current_number, i['title'], i['price'], i['img'])
    
    context = {'items' : gsDatas, 'name':name.upper()}

    return render(request, 'store/event-list.html',context)

# 이벤트 리스트
def showEvent(request, name):
    print('request :: ', request)
    print('storeName : ', name)

    items = []
    if (request.method == 'GET'):
        if (name == 'gs25'):
            items.append(selectAllGS())
        # if (name == 'cu'):
        #     items.append(getItemsByStore(ItemCu))

    print('items : ', list(items))

    if(len(items) > 0):
        context = {'items' : list(items[0]), 'name':name.upper()}

        #1. 화면 랜더
        # return render(request, 'store/event-list.html',context) 
        
        #2. json응답
        json_data = json.dumps(context)  
        return HttpResponse(json_data, content_type='application/json')    
    else:
        return render(request, 'store/error.html',{'message':'리스트가 없습니다'})



# 편의점 별 아이템 리스트 가져오기
def getItemsByStore(model):
    return model.objects.all()

