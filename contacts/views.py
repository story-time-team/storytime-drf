from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated 

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticated]

"""     def get_queryset(self, *args, **kwargs):
        return Contact.objects.all().filter(owner=self.request.user)

    def perform_create(self, *args, **kwargs):
        serializer.save(owner=self.request.user)
 
 """