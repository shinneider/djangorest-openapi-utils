from django.urls import path

from .settings import REDOC_ENABLE, REDOC_VIEW

app_name = 'redoc'

urlpatterns = []

if REDOC_ENABLE:
    urlpatterns.append(
        path('redoc', REDOC_VIEW(), name='redoc-template')
    )
