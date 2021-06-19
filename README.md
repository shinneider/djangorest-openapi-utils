Django Rest OpenAPI Utils
=============================

Improve your django-rest openapi schema

If you use or like the project, click `Star` and `Watch` to generate metrics and i evaluate project continuity.

# Install:

```
pip install djangorest-openapi-utils
```

# Usage:

1. Add to your INSTALLED_APPS, in settings.py:

   ```
   INSTALLED_APPS = [
       ...
       'djangorest_openapi_utils',
       ...
   ]
   ```
1. Add to your main urls.py

   ```
   urlpatterns = [
       ...
       # third part app's url's
       path('', include('django_openapi_utils.openapi.urls', namespace='openapi')),
       path('', include('django_openapi_utils.redoc.urls', namespace='redoc')), # Optinal (to use redoc)
       path('', include('django_openapi_utils.swagger.urls', namespace='swagger')), # Optinal (to use swagger)
       path('', include('django_openapi_utils.rapidoc.urls', namespace='rapidoc')) # Optinal (to use rapidoc)
       ...
   ]
   ```

1. Add to instaled apps settings:

    ```
    INSTALLED_APPS = [
        ...
        # Third part apps
        'django_openapi_utils.openapi',
        'django_openapi_utils.redoc',
        'django_openapi_utils.swagger',
        'django_openapi_utils.rapidoc',
        ...
    ]
    ```

1. Enable and configure feature in your settings:

    ```
    OPENAPI_ENABLE = True
    OPENAPI_CONFIGURATION = {
        'TITLE': 'Account MS',
        'DESCRIPTION': 'API Documentation',
        'VERSION': '1.0.0',
        'PUBLIC': True,  # show all url or just list read-only api's

        # https://swagger.io/specification/#tag-object
        'OPENAPI_TAGS': [],
        # https://swagger.io/docs/specification/api-host-and-base-path/
        'SERVERS': [] # is a dict {'url': 'http://...','desc': "Optional"} if empty add current running url to servers

        # https://swagger.io/docs/specification/authentication/
        'SECURITY_SCHEMES': {'bearerAuth': {'type': 'http', 'scheme': 'bearer', 'bearerFormat': 'JWT'}},
        'OPERATOR_SECURITY': [{'bearerAuth': []}],
    }
    REDOC_ENABLE = True
    REDOC_CONFIGURATION = {
        'TEMPLATE_TITLE': 'Your App Name',  # title of the page
        # 'OPENAPI_URL': 'http://...',  # To use external OpenAPI url
        # 'REDOC_VIEW': 'django_openapi_utils.redoc.view.ReDocView', # if you need to pass personalized vars to template
    }
    SWAGGER_ENABLE = True
    SWAGGER_CONFIGURATION = {
        'TEMPLATE_TITLE': 'Your App Name',  # title of the page
        # 'OPENAPI_URL': 'http://...',  # To use external OpenAPI url
        # 'REDOC_VIEW': 'django_openapi_utils.redoc.view.ReDocView', # if you need to pass personalized vars to template
    }
    RAPIDOC_CONFIGURATION = True
    RAPIDOC_CONFIGURATION = {
        'TEMPLATE_TITLE': 'Your App Name',  # title of the page
        # 'OPENAPI_URL': 'http://...',  # To use external OpenAPI url
        # 'REDOC_VIEW': 'django_openapi_utils.redoc.view.ReDocView', # if you need to pass personalized vars to template
    }
    ```

1. Improve your api specs

    ```
    from django_openapi_utils.openapi.schemas import OpenApiSchema

    class YourView(...):
        ...
        permission_classes = (IsAuthenticated, )  # use IsAuthenticated or IsAuthenticatedOrReadOnly subclasses to create 401 status code in OpenAPI
        schema = OpenApiSchema(
            tags=['Yout Tag'], # Optinal to agroup request in tags
        )
        openapi_id = 'Send Account Password Reset Email'
        openapi_description = 'Send Account Password Reset Email'
        openapi_enable_404_status_code = True  # to create 404 status code in OpenAPI
    ```

1. Multiple id/description for same router (If you have view with multiple routers Ex: RetrieveUpdateDestroyApiView)

    ```
    from django_openapi_utils.openapi.schemas import OpenApiSchema

    class YourView(...):
        ...
        schema = OpenApiSchema()
        
        def openapi_mount_description(self, path, method):
            return {'GET': 'Get ID', 'POST', 'Post ID', 'PUT': 'Put ID', 'PATCH': 'PATCH ID', 'DELETE': 'Delete ID'}[method]
        def get_object(self):
            return {'GET': 'Get Desc', 'POST', 'Post Desc', 'PUT': 'Put Desc', 'PATCH': 'PATCH Desc', 'DELETE': 'Delete Desc'}[method]
    ```

# Check Result

1. Access urls:
    1. `/redoc`
        ![image](https://user-images.githubusercontent.com/30196992/122618217-2fab6200-d064-11eb-9de7-2ac11d65efad.png)
    2. `/rapidoc`
        ![image](https://user-images.githubusercontent.com/30196992/122618278-510c4e00-d064-11eb-9cbb-24cef53aedd5.png)
    3. `/swagger`
        ![image](https://user-images.githubusercontent.com/30196992/122618340-7436fd80-d064-11eb-85f9-3372f04d3090.png)
