from django.db import models


class Ecole(models.Model):
    enseignant = models.CharField(default="test", max_length=5)
    titre = models.CharField(max_length=50, blank=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)

    def __str__(self):
        return f'{self.titre} by {self.enseignant}'


class Classe(models.Model):
    nom = models.CharField(max_length=20, blank=False)
    filliere = models.CharField(max_length=50)
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Questionnaire(models.Model):
    enregistreur = models.CharField(default="test", max_length=5)
    Otites_fréquentes = models.CharField(max_length=3)
    Angines_fréquentes = models.CharField(max_length=3)

    def __str__(self):
        return 'Questionnaire'


class Eleve(models.Model):
    nom = models.CharField(blank=False, max_length=50)
    prenom = models.CharField(null=True, blank=True, max_length=50)
    sexe = models.CharField(max_length=1)
    avatar = models.ImageField(null=True, blank=True)
    image_AN = models.ImageField(null=True, blank=True)  # Acte de naissance
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    questionnaire = models.OneToOneField(
        Questionnaire, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'nom: {self.nom} et prenom: {self.prenom}'


class Commentaire(models.Model):
    auteur = models.CharField(default="test", max_length=5)
    titre = models.CharField(blank=False, null=False, max_length=50)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
