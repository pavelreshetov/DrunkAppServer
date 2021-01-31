from django.http import JsonResponse
from PackService.controllers.QuestionAPI import QuestionApi
from PackService.models.QuestionModel import QuestionModel


class QuestionView:

    def get_questions(self, request):
        if request.method == "GET":
            try:
                response = QuestionApi().get_all_questions()
                return JsonResponse(data=response, status=200)
            except QuestionModel.DoesNotExist:
                return JsonResponse(data={}, status=404)
