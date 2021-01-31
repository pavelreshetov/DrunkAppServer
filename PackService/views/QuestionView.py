from django.http import JsonResponse
from PackService.controllers.QuestionAPI import QuestionApi
from PackService.models.QuestionModel import QuestionModel


class QuestionView:

    def get_questions(self, request):
        if request.method == "GET":
            response = QuestionApi().get_all_questions()
            if not response['data']:
                return JsonResponse(data={}, status=404)
            else:
                return JsonResponse(data=response, status=200)
        else:
            response = {
                "message": "Method not allowed"
            }
            return JsonResponse(data=response, status=405)
