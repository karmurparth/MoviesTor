from django.urls import path
from . import views

urlpatterns = [
    path('',views.hi,name='home-page' ),
    path('<name>/<no>/',views.result,name='search-result' ),
]