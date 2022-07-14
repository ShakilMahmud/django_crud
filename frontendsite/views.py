from django.shortcuts import render
from rest_framework import viewsets


# Create your views here.
def list(request):
   return render(request,'list.html')


# class PostPagination(PageNumberPagination):
#     page_size = 3

# class PostViewSet(viewsets.ModelViewSet):
#     pagination_class = PostPagination
#     serializer_class = TashSerializer
#     queryset = Task.objects.all()
