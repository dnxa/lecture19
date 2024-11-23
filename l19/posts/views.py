from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Post
# Create your views here.

def main_posts(request):
    if request.method == 'GET':
        # Create a list with sets of data
        result = [(i.title, i.description, i.author, i.comments, i.likes) for i in Post.objects.all()]

        # Our list is converted to json and sent as a response.
        return JsonResponse({"messages": result})
    else:
        return HttpResponse(content="Invalid request", status=400)

def create_posts(request):
    if request.method == 'GET':
        # This is supposed to have some ui for creating posts but i have no idea how to do that.
        return HttpResponse(content="This is supposed to allow you to create new posts, but I dont know how to do that...")
    else:
        return HttpResponse(content="Invalid request", status=400)