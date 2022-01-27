
from rest_framework import serializers
from biblioteca.models import Autor, Editor, Libro


class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = '__all__'


class EditorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Editor
        fields = '__all__'


class LibroListaSerializer(serializers.ModelSerializer):
    editor = EditorSerializer()
    autores = AutorSerializer(many=True)
    class Meta:
        model = Libro
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    #editor = EditorSerializer()
    #autores = AutorSerializer(many=True)
    class Meta:
        model = Libro
        fields = '__all__'