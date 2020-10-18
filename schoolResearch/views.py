from django.shortcuts import render, get_object_or_404
from django.http import Http404

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


from .models import (Ecole, Classe, Eleve, Questionnaire, Commentaire)
from .serialisers import (EcoleSerializer, ClasseSerializer,
                          EleveSerializer, QuestionnaireSerializer, CommentaireSerializer)


""" class EcoleTest(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'test': 'testos'}, status=HTTP_200_OK) """

# Ecole


class EcoleView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EcoleSerializer
    queryset = Ecole.objects.all()


# Classe


class ClasseListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ClasseSerializer

    def get_queryset(self):
        ecole_id = self.request.query_params.get('ecole', None)
        ecole = Ecole.objects.get(id=ecole_id)
        return Classe.objects.filter(ecole=ecole)


class ClasseCreateView(APIView):

    def post(self, request, *args, **kwargs):

        classes = request.data.get('classes', None)
        current_ecole = request.data.get('ecole', None)

        if (classes is None):
            return Response({"message": "There is not classes in your request"}, status=HTTP_400_BAD_REQUEST)
        else:
            if (current_ecole["id"]):
                ecole = Ecole.objects.get(id=current_ecole["id"])
            else:
                ecole = Ecole.objects.get(titre=current_ecole["titre"])
            for classe in classes:
                new = Classe(
                    nom=classe["nom"], filliere=classe["filliere"], ecole=ecole)
                new.save()
            return Response({"message": "Success"}, status=HTTP_200_OK)


# Eleve

class ElevesListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EleveSerializer

    def get_queryset(self):
        ecole_id = self.request.query_params.get('ecole', None)
        ecole = Ecole.objects.get(id=ecole_id)
        classes = Classe.objects.filter(ecole=ecole)
        print(list(classes))

        return Eleve.objects.filter(classe__in=classes)


class EleveCreateView(APIView):

    def post(self, request, *args, **kwargs):

        eleves = request.data.get('eleves', None)

        if (eleves is None):
            return Response({"message": "There is not eleves in your request"}, status=HTTP_400_BAD_REQUEST)
        else:
            for eleve in eleves:
                id_classe = eleve["classe"]["id"]
                classe = Classe.objects.get(id=id_classe)
                new = Eleve(
                    nom=eleve["nom"], prenom=eleve["prenom"], sexe=eleve["sexe"], classe=classe)
                new.save()
            return Response({"message": "Success"}, status=HTTP_200_OK)


# Questoinnaire
class AddQuestionnaireView(APIView):

    def post(self, request, *args, **kwargs):

        response = request.data.get('response', None)
        id_eleve = request.data.get('id', None)

        if (response is None):
            return Response({"message": "There is not response in your request"}, status=HTTP_400_BAD_REQUEST)
        else:
            print(id_eleve, response)
            questionnaire = Questionnaire(
                Otites_fréquentes=response["Otites_fréquentes"], Angines_fréquentes=response["Angines_fréquentes"])
            questionnaire.save()
            print(questionnaire)
            # update Eleve
            eleve = Eleve.objects.filter(id=id_eleve).update(
                questionnaire=questionnaire)
            return Response({"message": "Success"}, status=HTTP_200_OK)
