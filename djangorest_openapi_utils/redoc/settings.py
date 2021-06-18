from pydoc import locate

from django.conf import settings
from django.urls import reverse_lazy

_CONFIG = getattr(settings, 'REDOC_CONFIGURATION', {})


REDOC_ENABLE = getattr(settings, 'REDOC_ENABLE', False)
TEMPLATE_TITLE = _CONFIG.get('TEMPLATE_TITLE', 'ReDoc')
OPENAPI_URL = _CONFIG.get('OPENAPI_URL') or reverse_lazy('openapi:openapi-schema')
REDOC_VIEW = locate(_CONFIG.get('REDOC_VIEW', 'djangorest_openapi_utils.redoc.view.ReDocView.as_view'))
