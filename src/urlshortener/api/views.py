from urlshortener.api.serializer import ShortenerSerializer
from urlshortener.models import Shortened
from rest_framework.views import APIView
from django.views import View
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import redirect

# Create your views here.

class ShortenURL(APIView):
    """
        This endpoint receives a URL and returns a
        shortened version.
    """

    serializer_class = ShortenerSerializer

    @swagger_auto_schema(request_body=ShortenerSerializer)
    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        

        validated_data = serializer.save()

        if validated_data:
            return Response(
                {
                    'status': True,
                    'message': 'Successfully shortened URL {}.'.format(validated_data.original_url),
                    'data': validated_data.shortened_url
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
                {
                    'status': False,
                    'message': 'An error occured, try again later.'
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class ResolveShortenedURL(View):
    """
    Resolve shortened URL and redirect to original site.
    """

    def get(self, request, shortened_id):

        try:
            url = Shortened.objects.get(shortcode=shortened_id)
            return redirect(url.original_url)
        except Shortened.DoesNotExist:
            return HttpResponse('Invalid URL')
            
 