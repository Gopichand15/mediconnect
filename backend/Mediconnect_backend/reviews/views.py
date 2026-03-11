from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer

# List all reviews and create a new review
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Retrieve, update, or delete a specific review
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer