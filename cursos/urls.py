from django.urls import path

from .views import CursoAPIView, CursosAPIView, AvaliacaoAPIView, AvaliacoesAPIView

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'), # pk é primary key = o id
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'), # curso_pk é para saber que o id é do curso e nao de avaliações
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='curso_avaliacao'), 
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'), 
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]
