from django.urls import path
from urlshortener.api.views import (
    ShortenURL

)


urlpatterns = [

    path('generate/', ShortenURL.as_view(), name='generate_shortened_url'),

]

