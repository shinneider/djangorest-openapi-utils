from pydoc import locate

from django.conf import settings

from . import constants

_CONFIG = getattr(settings, 'OPENAPI_CONFIGURATION', {})

OPENAPI_ENABLE = getattr(settings, 'OPENAPI_ENABLE', False)

# Instance parameters
OPENAPI_TITLE = _CONFIG.get('TITLE', 'OpenApi URL')
OPENAPI_DESCRIPTION = _CONFIG.get('DESCRIPTION', 'Fast Django REST OpenApi')
OPENAPI_VERSION = _CONFIG.get('VERSION', '1.0.0 - Beta')
OPENAPI_PUBLIC = _CONFIG.get('PUBLIC', False)

OPENAPI_TAGS = _CONFIG.get('TAGS', [])
OPENAPI_SERVERS = _CONFIG.get('SERVERS', [])
# see https://swagger.io/docs/specification/authentication/
OPENAPI_SECURITY_SCHEMES = _CONFIG.get('SECURITY_SCHEMES', {})
OPENAPI_OPERATOR_SECURITY = _CONFIG.get('OPERATOR_SECURITY', None)
OPENAPI_ERROR_ON_SEND_LAYOUT = _CONFIG.get('ERROR_ON_SEND_LAYOUT', constants.ERROR_ON_SEND_LAYOUT)


def get_openapi_tags():
    return OPENAPI_TAGS


def set_openapi_tags(name, description):
    OPENAPI_TAGS.append({"name": name, "description": description})
