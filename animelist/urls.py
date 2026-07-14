from django.urls import path
from .views import home_page,detail_page,AnimeListView


urlpatterns=[
    path('list/',AnimeListView.as_view()),
    path('<int:pk>/',detail_page,name='detail')
]