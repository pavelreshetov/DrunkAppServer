from django.urls import path
from .views.PackView import PackView
from .views.QuestionView import QuestionView


urlpatterns = [
    path('pack', PackView().get_packs, name='pack'),
    path('question', QuestionView().get_questions, name='question')
]
