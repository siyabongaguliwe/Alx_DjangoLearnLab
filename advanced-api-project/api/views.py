from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# 📚 List all books (Read-only access for everyone)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# 📖 Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# 📝 Create a new book (Authenticated users only)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# ✏️ Update an existing book (Authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# ❌ Delete a book (Authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# BookListView: Returns all Book instances. Public access.
# BookDetailView: Returns a single Book by ID. Public access.
# BookCreateView: Allows authenticated users to create a Book.
# BookUpdateView: Allows authenticated users to update a Book.
# BookDeleteView: Allows authenticated users to delete a Book.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can create

from rest_framework import permissions

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view the list

from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
