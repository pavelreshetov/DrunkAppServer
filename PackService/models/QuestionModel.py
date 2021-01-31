from django.db import models


class QuestionModel(models.Model):
    question_id = models.AutoField(primary_key=True)
    pack_id = models.IntegerField()
    question = models.TextField()
    gender = models.IntegerField()

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return self.question

