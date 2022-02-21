from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Comment, Post
from .serializers import UserSerializer, CommentSerializer, PostSerializer

# Create your views here.

class PostList(APIView):
  queryset = Post.objects.all()

  def get(self, request):
    posts = list(self.queryset.all())
    posts = [PostSerializer(post).data['title'] for post in posts]
    return Response(posts)

class PostDetail(APIView):
  queryset = Post.objects.all()

  def get(self, request, pk):
    post = self.queryset.get(id=pk)
    post = PostSerializer(post).data
    return Response(post)

