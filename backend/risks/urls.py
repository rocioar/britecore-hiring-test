from django.urls import include, re_path

from rest_framework import routers

from risks import views

router = routers.DefaultRouter()

router.register(r'risk_type', views.RiskTypeViewSet)
router.register(r'field', views.FieldViewSet)
router.register(r'field_type', views.FieldTypeViewSet)

urlpatterns = [
    re_path(r'^', include((router.urls))),
]
