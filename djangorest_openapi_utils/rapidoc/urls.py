from django.urls import path

from .settings import RAPIDOC_ENABLE, RAPIDOC_VIEW

app_name = 'rapidoc'

urlpatterns = []

if RAPIDOC_ENABLE:
    urlpatterns.append(
        path('rapidoc', RAPIDOC_VIEW(), name='rapidoc-template')
    )
