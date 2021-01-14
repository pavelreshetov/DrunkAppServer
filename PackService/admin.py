from django.contrib import admin
from .models.packs import Packs
from .models.question_info import Questions

admin.site.register(Packs)
admin.site.register(Questions)