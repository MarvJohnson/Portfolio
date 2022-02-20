from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Comment, Post
from .serializers import UserSerializer, CommentSerializer, PostSerializer

# Create your views here.

class Test(APIView):
  queryset = Post.objects.all()

  def get(self, request):
    post = self.queryset.get()
    data = PostSerializer(post).data
    return Response(data)

