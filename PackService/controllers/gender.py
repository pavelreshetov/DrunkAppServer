def fill_gender(apps, schema_editor):
    genders = [
        (1, 'male'),
        (2, 'female'),
        (3, 'both')
    ]
    Gender = apps.get_model("PackService", "Gender")
    for gender in genders:
        add = Gender.objects.create(gender_id=gender[0], gender_name=gender[1])
        add.save()
