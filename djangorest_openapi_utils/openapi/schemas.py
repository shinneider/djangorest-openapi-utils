from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.schemas.openapi import AutoSchema, SchemaGenerator

from . import constants, settings


class OpenApiSchemaGenerator(SchemaGenerator):

    def get_server(self, request):
        servers = settings.OPENAPI_SERVERS
        if len(servers) == 0:
            servers = [
                {"url": f"{request.scheme}://{request.get_host()}"}
            ]
        return servers

    def get_schema(self, *args, **kwargs):
        schema = super().get_schema(*args, **kwargs)
        schema["servers"] = self.get_server(args[0])
        schema["tags"] = settings.OPENAPI_TAGS
        schema["components"]["securitySchemes"] = settings.OPENAPI_SECURITY_SCHEMES
        schema["components"]["schemas"]["ErrorOnSend"] = constants.ERROR_ON_SEND_LAYOUT
        return schema


class OpenApiSchema(AutoSchema):

    def get_operation_id(self, path, method):
        operation_id = getattr(self.view, 'openapi_id', None)
        if hasattr(self.view, 'openapi_mount_id'):
            return self.view.openapi_mount_id(path, method)
        return operation_id if operation_id else super().get_operation_id(path, method)

    def map_serializer(self, serializer):
        results = super().map_serializer(serializer)
        if apend_required := getattr(self.view, 'openapi_apend_required_fields', None):
            assert isinstance(apend_required, (list, tuple)), "`openapi_apend_required_fields` must be list or tuple."
            results['required'] = [*apend_required, *results['required']]

        return results

    def get_description(self, path, method):
        description = getattr(self.view, 'openapi_description', None)
        if hasattr(self.view, 'openapi_mount_description'):
            return self.view.openapi_mount_description(path, method)
        return description if description else super().get_description(path, method)

    def get_responses(self, path, method):
        responses = super().get_responses(path, method)

        if status_code := getattr(self.view, 'success_status_code', None):
            responses = {f'{status_code}':  responses[list(responses.keys())[0]]}

        view_permissions = getattr(self.view, 'permission_classes', [None, ])
        has_auth_class = len(view_permissions) > 0
        safe_path = path not in SAFE_METHODS
        if has_auth_class and issubclass(view_permissions[0], IsAuthenticated):
            responses['401'] = {"description": "Authentication credentials were not provided."}

        if has_auth_class and issubclass(view_permissions[0], IsAuthenticatedOrReadOnly) and safe_path:
            responses['401'] = {"description": "Authentication credentials were not provided."}

        if method in ['POST', 'PUT', 'PATCH']:
            responses['400'] = {
                "description": "One or more filled fields or bussiness logic are invalid.",
                "content": {
                    ct: {'schema': {'$ref': '#/components/schemas/ErrorOnSend'}}
                    for ct in self.request_media_types
                }
            }

        if getattr(self.view, 'openapi_enable_404_status_code', False):
            responses['404'] = {"description": "Object or entity not found."}

        # view_permissions = getattr(self.view, 'permission_classes', [None, ])
        # if issubclass(view_permissions[0], IsAuthenticated):
        #     responses['403'] = {"description": "You are not allowed to perform this action."}

        return responses

    def get_components(self, path, method):
        components = super().get_components(path, method)
        return components

    def get_operation(self, path, method):
        operation = super().get_operation(path, method)
        
        view_permissions = getattr(self.view, 'permission_classes', [None, ])
        has_auth_class = len(view_permissions) > 0
        if has_auth_class and issubclass(view_permissions[0], IsAuthenticated):
            security = settings.OPENAPI_OPERATOR_SECURITY
            if security is None:
                security = [{x: []} for x in list(settings.OPENAPI_SECURITY_SCHEMES.keys())]
            operation['security'] = security

        return operation
