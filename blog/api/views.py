from main.models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer


# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
    api_urls={
        'List':'/post-list/',
        'Detail View':'/post-detail/<str:pk>/',
        'Create': '/post-creat/',
        'Update': '/post-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def postList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def postDetail(request,pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def postCreate(request):
    serializer=PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def postUpdate(request,pk):
    post = Post.objects.get(id=pk)
    serializer=PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def postDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return Response('Succesfully deleted!')