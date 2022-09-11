from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


from .models import Goal
from .serializers import GoalSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import generics

class GoalViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()
    
    
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class GoalDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
