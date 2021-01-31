from django.db import models


class PackModel(models.Model):
    pack_id = models.AutoField(primary_key=True)
    pack_name = models.TextField()

    class Meta:
        db_table = 'packs'

    def __str__(self):
        return self.pack_name
