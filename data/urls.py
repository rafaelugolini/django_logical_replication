from django.conf.urls import url, include
from rest_framework import routers

from .views import DataViewSet, AnnotationViewSet


router = routers.DefaultRouter()
router.register(r'data', DataViewSet, base_name='data')
router.register(r'annotation', AnnotationViewSet, base_name='annotation')

urlpatterns = [
    url(r'^', include(router.urls))
]
