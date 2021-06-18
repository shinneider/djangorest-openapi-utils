from django.urls import path

from .settings import SWAGGER_ENABLE, SWAGGER_VIEW

app_name = 'swagger'

urlpatterns = []

if SWAGGER_ENABLE:
    urlpatterns.append(
        path('swagger', SWAGGER_VIEW(), name='swagger-template')
    )
