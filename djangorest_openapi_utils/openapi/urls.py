from re import I

from django.conf import settings
from django.urls import path
from rest_framework.schemas import get_schema_view
from rest_framework.settings import api_settings

from . import settings
from .schemas import OpenApiSchemaGenerator

app_name = 'openapi'

urlpatterns = []

if getattr(settings, 'OPENAPI_ENABLE', False):
    urlpatterns.append(
        path('openapi', get_schema_view(
            title=settings.OPENAPI_TITLE,
            description=settings.OPENAPI_DESCRIPTION,
            version=settings.OPENAPI_VERSION,
            public=settings.OPENAPI_PUBLIC,
            renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES,
            generator_class=OpenApiSchemaGenerator
        ), name='openapi-schema')
    )
