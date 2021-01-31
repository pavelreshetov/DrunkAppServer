from PackService.models.QuestionModel import QuestionModel


class QuestionApi:

    def get_all_questions(self):
        response = {
            "data": []
        }
        for question in QuestionModel.objects.all():
            question_struct = {
                "question_id": question.pk,
                'question': question.question,
                'gender': question.gender,
                'pack_id': question.pack_id
            }
            response["data"].append(question_struct)
        return response

