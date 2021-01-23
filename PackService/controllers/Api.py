from PackService.models.packs import Packs
from PackService.models.question_info import Questions


def all_packs():
    data = {}
    packs = Packs.objects.all()
    for pack in packs:
        data[pack.pack_id] = {'pack_name': pack.pack_name}

    return data


def all_questions():
    data = {}
    questions = Questions.objects.all()
    for question in questions:
        data[question.question_id] = {
            'pack_id': question.pack_id,
            'question': question.question,
            'gender': question.gender
        }

    return data

