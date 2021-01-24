from django.http import JsonResponse
from PackService.controllers.api_question import QuestionApi


class Questions:

    def questions(self, request):
        if request.method == "GET":
            data = {
                'data': QuestionApi.all_questions()
            }
            return JsonResponse(data=data, status=200)
        else:
            answer = 'method did not find'
            return answer


