from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Book, Review, Comment, Like
from .serializers import UserSerializer, BookSerializer, ReviewSerializer, CommentSerializer, LikeSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status

# User registration
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({"refresh": str(refresh), "access": str(refresh.access_token)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Book CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Review CRUD
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        review = self.get_object()
        like, created = Like.objects.get_or_create(review=review, user=request.user)
        return Response({"liked": True})

    @action(detail=True, methods=['delete'])
    def unlike(self, request, pk=None):
        review = self.get_object()
        Like.objects.filter(review=review, user=request.user).delete()
        return Response({"liked": False})

# Comment CRUD
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

