from django.db import models


class Questions(models.Model):
    question_id = models.AutoField(primary_key=True)
    pack_id = models.IntegerField()
    question = models.TextField()
    gender = models.IntegerField()

    def __str__(self):
        return self.question

