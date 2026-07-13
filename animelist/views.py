from django.shortcuts import render
from .models import Anime
from django.db.models import Q

def home_page(request):
    animes=Anime.objects.all()
    query = request.GET.get('q', '')
    if query:
        articles = Anime.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return render(request, 'search.html', {"articles": articles})
    context={
        "animes":animes
    }
    return render(request,'home.html',context)

def detail_page(request,pk):
    tavsif=Anime.objects.get(pk=pk)
    return render(request,'detail.html',{"tavsif":tavsif})

