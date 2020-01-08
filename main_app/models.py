# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Client(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=100)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=100)  # Field name made lowercase.
    num_rue = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    email = models.CharField(max_length=100)
    date_naissance = models.DateField()
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "{id:" + self.id.__str__() + ",nom:" + self.nom + ",prenom:" + self.prenom +  ",date_naissance" + self.date_naissance.__str__() + ",email:" + self.email + ",login:" + self.login + ",password:" + self.password + "}"

    class Meta:
        managed = False
        db_table = 'Client'


class Commande(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    etat = models.CharField(max_length=200)
    reservation = models.ForeignKey('Reservation', models.DO_NOTHING)
    menu = models.ForeignKey('Menu', models.DO_NOTHING, db_column='Menu_id')  # Field name made lowercase.
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')

    class Meta:
        managed = False
        db_table = 'Commande'


class Element(models.Model):
    libelle = models.CharField(db_column='Libelle', max_length=200)  # Field name made lowercase.
    type = models.CharField(max_length=14)
    menu = models.ForeignKey('Menu', models.DO_NOTHING)
    prix = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Element'


class Menu(models.Model):
    libelle = models.CharField(db_column='Libelle', max_length=200)  # Field name made lowercase.
    prix_total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Menu'


class Proprietaire(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=100)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=100)  # Field name made lowercase.
    num_rue = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    email = models.CharField(max_length=100)
    date_naissance = models.DateField()
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Proprietaire'


class Reservation(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    nb_personnes = models.IntegerField()
    etat = models.CharField(max_length=200)
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')

    class Meta:
        managed = False
        db_table = 'Reservation'


class ReservationTables(models.Model):
    reservation = models.OneToOneField(Reservation, models.DO_NOTHING, db_column='reservation', primary_key=True)
    table = models.ForeignKey('Table', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Reservation_tables'
        unique_together = (('reservation', 'table'),)


class Table(models.Model):
    numero_table = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Table'
