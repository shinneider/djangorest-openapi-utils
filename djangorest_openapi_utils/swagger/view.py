from django.views.generic import TemplateView

from .settings import OPENAPI_URL, TEMPLATE_TITLE


class SwaggerView(TemplateView):
    template_name = 'swagger/swagger.html'

    def get_context_data(self, **kwargs):
        return {
            'OPENAPI_URL': OPENAPI_URL,
            'TITLE': TEMPLATE_TITLE
        }
