from django.db import models


class Packs(models.Model):
    pack_id = models.AutoField(primary_key=True)
    pack_name = models.TextField()

    def __str__(self):
        return self.pack_name
