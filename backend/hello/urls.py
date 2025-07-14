from django.urls import path
from . import views

urlpatterns = [
    # Web views
    path('', views.hello_world, name='hello_world'),
    path('template/', views.hello_template, name='hello_template'),
    
    # API endpoints
    path('api/hello/', views.api_hello, name='api_hello'),
    path('api/greetings/', views.GreetingListCreateView.as_view(), name='greeting-list-create'),
    path('api/greetings/<int:pk>/', views.GreetingDetailView.as_view(), name='greeting-detail'),
]
