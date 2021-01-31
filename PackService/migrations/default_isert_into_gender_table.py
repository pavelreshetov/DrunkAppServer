from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PackService', 'default_create_gender_table'),
    ]

    operations = [
        migrations.RunSQL(
            "INSERT INTO genders (gender_id, gender_name) "
            "VALUES (1, 'male'), (2, 'female'), (3, 'both')"
        ),
    ]

