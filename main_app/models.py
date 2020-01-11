# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Client(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=100)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=100)  # Field name made lowercase.
    adresse = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "{id:" + self.id.__str__() + ",nom:" + self.nom + ",prenom:" + self.prenom + ",adresse:" + self.adresse + ",email:" + self.email + ",login:" + self.login + ",password:" + self.password + "}"

    class Meta:
        managed = False
        db_table = 'Client'


class Element(models.Model):
    libelle = models.CharField(db_column='Libelle', max_length=200)  # Field name made lowercase.
    type = models.CharField(max_length=200)
    menu = models.ForeignKey('Menu', models.DO_NOTHING)
    prix = models.FloatField()
    img_url = models.CharField(max_length=200)

    def __str__(self):
        return "{id:" + self.id.__str__() + ",libelle:" + self.libelle + ",type:" + self.type + ",prix:" + self.prix.__str__() + ",menuid:" + self.menu.id.__str__() +",img_url:"+self.img_url+ "}"

    class Meta:
        managed = False
        db_table = 'Element'


class Menu(models.Model):
    libelle = models.CharField(db_column='Libelle', max_length=200)  # Field name made lowercase.
    prix_total = models.FloatField(blank=True, null=True)
    titre = models.CharField(max_length=100)
    type=models.CharField(max_length=100)

    def __str__(self):
        return "{id:" + self.id.__str__() + ",libelle:" + self.libelle + ",prix_total:" + self.prix_total.__str__() + ",type:"+self.type+"}"

    class Meta:
        managed = False
        db_table = 'Menu'


class Proprietaire(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=100)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=100)  # Field name made lowercase.
    adresse = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "{id:" + self.id.__str__() + ",nom:" + self.nom + ",prenom:" + self.prenom + ",adresse:" + self.adresse + ",email:" + self.email +  ",login:" + self.login + ",password:" + self.password + "}"

    class Meta:
        managed = False
        db_table = 'Proprietaire'


class Reservation(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    nb_personnes = models.IntegerField()
    etat = models.CharField(max_length=200)
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')

    def __str__(self):
        return "{id:" + self.id.__str__() + ",date:" + self.date.__str__() + ",heure:" + self.heure.__str__() + ",nb_personnes:" + self.nb_personnes.__str__() + ",etat:" + self.etat + "}"

    class Meta:
        managed = False
        db_table = 'Reservation'


class Commande(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    etat = models.CharField(max_length=200)
    reservation = models.ForeignKey(Reservation, models.DO_NOTHING)
    menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='Menu_id')  # Field name made lowercase.
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')

    def __str__(self):
        return "{id:" + self.id.__str__() + ",date:" + self.date.__str__() + ",heure:" + self.heure.__str__() + ",etat:" + self.etat + "reservation:" + self.reservation.id.__str__() + ",menu:" + self.menu.id.__str__() + "}"

    class Meta:
        managed = False
        db_table = 'commande'
