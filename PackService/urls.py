from django.urls import path
from .views.pack import Packs
from .views.question import Questions


urlpatterns = [
    path('pack', Packs().get_packs, name='pack'),
    path('question', Questions().questions, name='question')
]
