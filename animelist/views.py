from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Anime


def home_page(request):
    animes = Anime.objects.all()
    query = request.GET.get('q', '')
    if query:
        articles = Anime.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return render(request, 'search.html', {"articles": articles})
    context = {"animes": animes}
    return render(request, 'home.html', context)


def detail_page(request, pk):
    tavsif = get_object_or_404(Anime, pk=pk)
    return render(request, 'detail.html', {"tavsif": tavsif})