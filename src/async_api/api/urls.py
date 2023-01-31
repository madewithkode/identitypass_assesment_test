from django.urls import path
from async_api.api.views import (
    FetchExternalData

)


urlpatterns = [
    path('', FetchExternalData.as_view(), name='fetch_external_data'),
]

