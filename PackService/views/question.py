from django.http import JsonResponse
from PackService.controllers.Api import all_questions


class Questions:

    def questions(self, request):
        if request.method == "GET":
            data = all_questions()

        return JsonResponse(data=data, status=200)


