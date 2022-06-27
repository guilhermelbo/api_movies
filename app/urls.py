from django.urls import path
from app import views

urlpatterns = [
    path('', views.movies_list),
    path('<int:pk>/', views.movies_detail_change_delete)
]