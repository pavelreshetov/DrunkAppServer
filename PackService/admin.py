from django.contrib import admin
from .models.PackModel import PackModel
from .models.QuestionModel import QuestionModel

admin.site.register(PackModel)
admin.site.register(QuestionModel)