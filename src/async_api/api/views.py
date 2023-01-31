from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from async_api.api_adapter import ExternalAPIdapter
import asyncio

class FetchExternalData(APIView):
    """
    Fetch external data from multiple source 
    return an aggregated response.
    """

    @swagger_auto_schema()
    def get(self, request):

        API_CLIENT = ExternalAPIdapter(['https://randomuser.me/api/', 'https://quotable.io/quotes?page=1'])

        try: 
            data = asyncio.run(API_CLIENT.fetch())
            return Response(
                {
                    'status': True,
                    'data': data
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    'status': False,
                    'message': 'An error occured: {}, try again later.'.format(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
            
 