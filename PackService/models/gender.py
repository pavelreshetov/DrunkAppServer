from django.db import models


class Gender(models.Model):
    gender_id = models.AutoField(primary_key=True)
    gender_name = models.TextField()

    def __str__(self):
        return self.gender_name
