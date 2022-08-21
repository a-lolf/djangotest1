from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class Apple(View):

    def get(self, request):
        try:
            request_data = request.GET
            return JsonResponse({'res': request_data})

        except Exception as e:
            return JsonResponse({'res': str(e)})
