from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('gender_id', models.AutoField(primary_key=True, serialize=False)),
                ('gender_name', models.TextField()),

            ],
            options={
                'db_table': 'genders',
            },
        ),
    ]
