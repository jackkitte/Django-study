from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, IsAuthenticated
)


from shop.models import Book
from .serializers import (
    BookSerializer, UserSerializer
)


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
