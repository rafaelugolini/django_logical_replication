from django.conf import settings

from rest_framework import viewsets
from rest_framework import permissions

from .models import Data, Annotation
from .serializers import DataSerializer, AnnotationSerializer


# Permisions

class PubSubDataPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # SUBSCRIBER shouldn't create data
        if settings.SUBSCRIBER and request.method in permissions.SAFE_METHODS:
            return True
        pub_methods = [*permissions.SAFE_METHODS, 'POST']
        # PUBLISHER can create data but can't edit
        if not settings.SUBSCRIBER and request.method in pub_methods:
            return True
        return False


# Views

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [PubSubDataPermission]


class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
