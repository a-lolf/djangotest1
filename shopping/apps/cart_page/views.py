from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.

class CartView(APIView):

    def get(self, request):
        try:
            chat_id = request.META.get('HTTP_CHAT_ID')
            request_data = request.GET
            mobile = request_data.get('mobile')
            client_name = request_data.get('client_name')

            return JsonResponse({'res': 'CartView API error'})

        except Exception as e:
            return JsonResponse({'res': str(e)})
