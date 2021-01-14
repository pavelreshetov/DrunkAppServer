from django.http import JsonResponse


class Test:

    def test(self, request):
        if request.method == "GET":
            data = {
                "name": "sasha"
            }
            return JsonResponse(data=data, status=200)
