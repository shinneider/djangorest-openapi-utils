from pydoc import locate

from django.conf import settings
from django.urls import reverse_lazy

_CONFIG = getattr(settings, 'RAPIDOC_CONFIGURATION', {})


RAPIDOC_ENABLE = getattr(settings, 'RAPIDOC_ENABLE', False)
TEMPLATE_TITLE = _CONFIG.get('TEMPLATE_TITLE', 'RapiDoc')
OPENAPI_URL = _CONFIG.get('OPENAPI_URL') or reverse_lazy('openapi:openapi-schema')
RAPIDOC_VIEW = locate(_CONFIG.get('RAPIDOC_VIEW', 'djangorest_openapi_utils.rapidoc.view.RapiDocView.as_view'))
