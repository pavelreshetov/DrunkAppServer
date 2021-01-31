from django.http import JsonResponse
from PackService.controllers.PackAPI import PackAPI
from PackService.models.PackModel import PackModel


class PackView:

    def get_packs(self, request):
        if request.method == "GET":
            try:
                response = PackAPI().get_all_packs()
                return JsonResponse(data=response, status=200)
            except PackModel.DoesNotExist:
                return JsonResponse(data={}, status=404)
