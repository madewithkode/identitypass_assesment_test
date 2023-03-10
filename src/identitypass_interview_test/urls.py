"""identitypass_interview_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.contrib.staticfiles.urls import static
from urlshortener.api.views import ResolveShortenedURL

schema_view = get_schema_view(
    openapi.Info(
        title="Identitypass APIs",
        default_version='v1',
        description="Documentation for Identitypass Interview Test APIs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="princekelvin91@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    
)

urlpatterns = [
    path('<str:shortened_id>/', ResolveShortenedURL.as_view(), name='resolve_url'),
    path('admin/', admin.site.urls),
    path('api/v1/shortener/', include(('urlshortener.api.urls', 'urlshortener'), namespace='urlshortener')),
    path('api/v1/async/', include(('async_api.api.urls', 'async_api'), namespace='async_api')),
    re_path(r'^api/docs/(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^api/docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)