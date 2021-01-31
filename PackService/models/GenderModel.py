from django.db import models


class GenderModel(models.Model):
    gender_id = models.AutoField(primary_key=True)
    gender_name = models.TextField()

    class Meta:
        db_table = 'genders'


    def __str__(self):
        return self.gender_name
