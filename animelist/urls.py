from django.urls import path
from .views import (home_page,detail_page,AnimeListView,AnimeRetrieveView,
                    AnimeDestroyView,AnimeCreateView,AnimeUpdateView)


urlpatterns=[
    path('list/',AnimeListView.as_view()),
    path('delete/<int:pk>/',AnimeDestroyView.as_view()),
    path('create/',AnimeCreateView.as_view()),
    path('update/<int:pk>/',AnimeUpdateView.as_view()),
    path('detail/<int:pk>/',AnimeRetrieveView.as_view()),
    path('<int:pk>/',detail_page,name='detail')
]