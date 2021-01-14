from django.db import models


class Questions(models.Model):
    question_id = models.AutoField(primary_key=True)
    pack_id = models.IntegerField()
    question = models.TextField()

    LOAN_STATUS = (
        ('m', 'male'),
        ('f', 'female'),
        ('b', 'both')
    )

    gender = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True)

    def __str__(self):
        return self.question

