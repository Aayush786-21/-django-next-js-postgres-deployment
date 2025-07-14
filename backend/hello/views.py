from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Greeting
from .serializers import GreetingSerializer

# Create your views here.
def hello_world(request):
    return HttpResponse("<h1>Hello World from Django + PostgreSQL!</h1>")

def hello_template(request):
    context = {'message': 'Hello World from Django + PostgreSQL!'}
    return render(request, 'hello/index.html', context)

# API Views
@api_view(['GET'])
def api_hello(request):
    """Simple hello API endpoint"""
    return Response({
        'message': 'Hello World from Django + PostgreSQL API!',
        'status': 'success'
    })

class GreetingListCreateView(generics.ListCreateAPIView):
    """List all greetings or create a new greeting"""
    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer

class GreetingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a specific greeting"""
    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer
