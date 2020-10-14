from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('<int:pk>', views.FurnitureDetailView.as_view(),name='furniture_pk'),
]
