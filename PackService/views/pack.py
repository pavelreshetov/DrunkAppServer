from django.http import JsonResponse
from PackService.controllers.Api import all_packs


class Packs:

    def packs(self, request):
        if request.method == "GET":
            data = all_packs()

        return JsonResponse(data=data, status=200)
