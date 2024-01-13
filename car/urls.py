from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_car, name='add_car'),
    path('details/<int:id>/', views.DetailCarView.as_view(), name='detail_car'),
]