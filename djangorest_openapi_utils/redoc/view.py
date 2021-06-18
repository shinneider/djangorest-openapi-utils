from django.views.generic import TemplateView

from .settings import OPENAPI_URL, TEMPLATE_TITLE


class ReDocView(TemplateView):
    template_name = 'redoc/redoc.html'

    def get_context_data(self, **kwargs):
        return {
            'OPENAPI_URL': OPENAPI_URL,
            'TITLE': TEMPLATE_TITLE
        }
