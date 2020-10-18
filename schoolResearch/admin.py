from django.contrib import admin
from .models import (Ecole, Classe, Eleve, Questionnaire, Commentaire)

admin.site.register(Ecole)
admin.site.register(Classe)
admin.site.register(Eleve)
admin.site.register(Questionnaire)
admin.site.register(Commentaire)