from django.http import JsonResponse
from PackService.controllers.PackAPI import PackAPI
from PackService.models.PackModel import PackModel


class PackView:

    def get_packs(self, request):
        if request.method == "GET":
            response = PackAPI().get_all_packs()
            if not response['data']:
                return JsonResponse(data={}, status=404)
            else:
                return JsonResponse(data=response, status=200)
        else:
            response = {
                "message": "Method not allowed"
            }
            return JsonResponse(data=response, status=405)
