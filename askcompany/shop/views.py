from django.shortcuts import render
from django.http import HttpResponse
from .models import Item


def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))


def item_list(request):
    q5 = Item.objects.all()
    q = request.GET.get('q', '')  # get인자에서 가져옴. q를 가져오는데, 없으면 빈 것을 반환하겠다
    if q:  # 즉 검색어가 있다면.
        # i = ignore, 즉 알파벳일 경우에는 대소문자를 구분하지 않겠다.
        q5 = q5.filter(name__icontains=q)
    return render(request, 'shop/item_list.html', {'item_list': q5, 'q': q})
