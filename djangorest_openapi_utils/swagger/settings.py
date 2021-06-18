from pydoc import locate

from django.conf import settings
from django.urls import reverse_lazy

_CONFIG = getattr(settings, 'SWAGGER_CONFIGURATION', {})


SWAGGER_ENABLE = getattr(settings, 'SWAGGER_ENABLE', False)
TEMPLATE_TITLE = _CONFIG.get('TEMPLATE_TITLE', 'ReDoc')
OPENAPI_URL = _CONFIG.get('OPENAPI_URL') or reverse_lazy('openapi:openapi-schema')
SWAGGER_VIEW = locate(_CONFIG.get('SWAGGER_VIEW', 'djangorest_openapi_utils.swagger.view.SwaggerView.as_view'))
