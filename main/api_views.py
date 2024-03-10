from main.models import ShortURL
from main.serializers import ShortURLSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework import status
class ShortURLListCreateView(generics.ListCreateAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class forwartAPIView(APIView):

    def get(self, request, short_url, format=None):
        try:
            short_url = f"http://localhost:8000/{short_url}/"
            short_url = ShortURL.objects.get(short_url=short_url)
            print(short_url)
            if short_url:
                return HttpResponseRedirect(redirect_to=short_url.url)
        except ShortURL.DoesNotExist:
            return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)