from datetime import datetime
from email.policy import default
from rest_framework import serializers
from urlshortener.models import Shortened
import os
from django.conf import settings
from urlshortener.utils import generate_shortened_url
import requests
from rest_framework import status


class ShortenerSerializer(serializers.Serializer):
    """
        Request serializer for creating new shortened URLS.
    """

    url = serializers.URLField(required=True)

    def validate(self, attrs):
        # Confirm that URL being provided is actully valid
        try:
            response = requests.get(attrs.get('url'))
            if not response.status_code == status.HTTP_200_OK:
                raise serializers.ValidationError(
                        "Unable to shorten URL, it does not appear return a success response."
                    )
        except Exception as e:
            raise serializers.ValidationError(
                        "Unable to shorten URL, it does not appear return a success response."
                    )

        return attrs

    def create(self, validated_data):
        
        # Generate unique URL
        try:
            latest_obj = Shortened.objects.latest('id')
            latest_obj_id = latest_obj.id
        except Shortened.DoesNotExist:
            latest_obj_id = 0
        unique_code  =  generate_shortened_url(latest_obj_id)
        
        try:
            return Shortened.objects.create(
                original_url = validated_data['url'],
                shortcode = unique_code,
                shortened_url = '{}{}/'.format(settings.BASE_URL, unique_code)
            )
        except Exception as e:
            raise serializers.ValidationError("An error ocured while shortening url {}".format(e))


