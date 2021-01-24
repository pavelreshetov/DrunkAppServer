from django.db import models, migrations
from PackService.controllers.gender import fill_gender


class Migration(migrations.Migration):

    dependencies = [
        ('PackService', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_gender),
    ]