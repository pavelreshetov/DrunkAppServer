from PackService.models.question_info import Questions


class QuestionApi:

    def all_questions():
        data = {}
        try:
            for question in Questions.objects.all():
                data[question.question_id] = {
                    'pack_id': question.pack_id,
                    'question': question.question,
                    'gender': question.gender
                }
            return data
        except Exception:
            return 'not found'
