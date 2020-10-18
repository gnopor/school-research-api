from django.urls import path
from .views import (
    EcoleView,
    ClasseCreateView,
    ClasseListView,
    EleveCreateView,
    ElevesListView,
    AddQuestionnaireView
)


urlpatterns = [
    path('ecole/', EcoleView.as_view(), name='ecole'),
    path('createClasses/', ClasseCreateView.as_view(), name="create-classes"),
    path('listClasses/', ClasseListView.as_view(), name="list-classes"),
    path('createEleves/', EleveCreateView.as_view(), name="create-eleves"),
    path('listEleves/', ElevesListView.as_view(), name="list-eleves"),
    path('addQuestionnaire/', AddQuestionnaireView.as_view(),
         name="add-questionnaire")
]
