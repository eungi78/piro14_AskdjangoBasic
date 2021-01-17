from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item


def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))


def item_list(request):
    items = Item.objects.all()
    # get인자에서 가져옴. word를 가져오는데, 없으면 빈 것을 반환하겠다
    word = request.GET.get('word', '')
    if word:  # 즉 검색어가 있다면.
        # i = ignore, 즉 알파벳일 경우에는 대소문자를 구분하지 않겠다.
        items = items.filter(name__icontains=word)
    return render(request, 'shop/item_list.html', {'items': items, 'word': word})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {'item': item})
