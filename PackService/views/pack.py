from django.http import JsonResponse
from PackService.controllers.api_pack import PackApi


class Packs:

    def get_packs(self, request):
        if request.method == "GET":
            data = {
                'data': PackApi.all_packs()
            }
            return JsonResponse(data=data, status=200)
        else:
            answer = 'method did not find'
            return answer
