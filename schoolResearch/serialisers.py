from rest_framework import serializers
from .models import (Ecole, Classe, Eleve, Questionnaire, Commentaire)

# Ecole


class EcoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecole
        fields = (
            'id',
            'enseignant',
            'titre',
            'latitude',
            'longitude'
        )

# Classe


class ClasseSerializer(serializers.ModelSerializer):
    ecole = serializers.SerializerMethodField()

    class Meta:
        model = Classe
        fields = (
            'id',
            'nom',
            'filliere',
            'ecole'
        )

    def get_ecole(self, obj):
        return EcoleSerializer(obj.ecole).data


# Questionnaire
class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = (
            'id',
            'enregistreur',
            'Otites_fréquentes',
            'Angines_fréquentes'
        )

# Eleve


class EleveSerializer(serializers.ModelSerializer):
    classe = serializers.SerializerMethodField()
    questionnaire = serializers.SerializerMethodField()

    class Meta:
        model = Eleve
        fields = (
            'id',
            'nom',
            'prenom',
            'sexe',
            'avatar',
            'image_AN',
            'classe',
            'questionnaire'
        )

    def get_classe(self, obj):
        return ClasseSerializer(obj.classe).data

    def get_questionnaire(self, obj):
        return QuestionnaireSerializer(obj.questionnaire).data

# Commantaire


class CommentaireSerializer(serializers.ModelSerializer):
    questionnaire = serializers.ModelSerializer()

    class Meta:
        model = Commentaire
        fields = (
            'id',
            'auteur',
            'titre',
            'questionnaire'
        )

        def get_questionnaire(self, obj):
            return QuestionnaireSerializer(obj.questionnaire).data
