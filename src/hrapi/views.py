# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
# from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

from .models import Log, Project
from .serializers import LogSerializer, ProjectSerializer
from .filters import LogListFilters
from .permissions import IsOwnerOrReadOnly

# Create your views here.



class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                         IsAdminUser)
    lookup_field = 'id'
    lookup_url_kwarg = "id"

class LogListView(generics.ListCreateAPIView):
    filter_class = LogListFilters
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly, IsAdminUser)
    lookup_field = 'id'
    lookup_url_kwarg = "id"
