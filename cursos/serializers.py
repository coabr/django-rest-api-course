from rest_framework import serializers
from django.db.models import Avg

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True} # write_only: True significa que o campo não será exibido na consulta, por segurança
        }
        model = Avaliacao
        fields = (
            'id', 
            'curso', 
            'nome', 
            'email', 
            'comentario', 
            'avaliacao', 
            'criacao', 
            'ativo'
        )

    def validate_avaliacao(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError('A avaliação deve estar entre 1 e 5')
class CursoSerializer(serializers.ModelSerializer):
    # 1 - Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True) # novo atributo que tras todas as informações de cada item
    
    # 2 - Hyperlinked Relationship
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail') # mostra um hyperlink para o item

    # 3 - Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # ideal pra grandes quantidades pq só mostra o ID do item

    media_avaliacoes = serializers.SerializerMethodField() # novo atributo que traz a média das avaliações

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media, 1)  