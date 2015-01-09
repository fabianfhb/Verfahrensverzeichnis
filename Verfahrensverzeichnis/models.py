#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils import encoding
from datetime import datetime

# Create your models here.

class Gruppe(models.Model):
    bezeichnung = models.CharField(max_length=30)

    def __unicode__(self):
        return self.bezeichnung


class Person(models.Model):
    name = models.CharField(max_length=30)
    vorname = models.CharField(max_length=30)
    gruppen = models.ManyToManyField(Gruppe, null=True, blank=True)
    zugriffberechtigt = models.BooleanField(default=None)

    def __unicode__(self):
        return "{} {}".format(self.name, self.vorname)


class Empfaenger(models.Model):
    is_drittstaat = models.BooleanField(default=None)
    bezeichnung = models.CharField(max_length=255)

    def __unicode__(self):
        return self.bezeichnung


class Inhalt(models.Model):
    bezeichnung = models.CharField(max_length=255)

    def __unicode__(self):
        return self.bezeichnung


class Herkunft(models.Model):
    bezeichnung = models.CharField(max_length=255)
    is_drittland = models.BooleanField(default=None)

    def __unicode__(self):
        return self.bezeichnung


class Betroffenenkreis(models.Model):
    bezeichnung = models.CharField(max_length=255)

    def __unicode__(self):
        return self.bezeichnung


class EmpfaengerPeriodizitaet(models.Model):
    empfaenger = models.ForeignKey(Empfaenger)
    periodizitaet = models.CharField(max_length=30)

    def __unicode__(self):
        return "{} ({})".format(self.empfaenger, self.periodizitaet)


class Verfahren(models.Model):
    lfdNr = models.AutoField(primary_key=True)
    bezeichnung = models.CharField(max_length=255)
    inhalt = models.ManyToManyField(Inhalt, )
    geschuetzt = models.BooleanField(default=None, verbose_name="geschützt")
    personen = models.ManyToManyField(Person, blank=True, null=True, verbose_name="Zugriffsberechtigte Personen")
    gruppen = models.ManyToManyField(Gruppe, blank=True, null=True, verbose_name="Zugriffsberechtigte Gruppen")
    herkunft = models.ForeignKey(Herkunft, blank=True, null=True, verbose_name="Herkunft der Daten")
    periodizitaet = models.CharField(max_length=30, blank=True, null=True, verbose_name="Periodizität der Daten")
    sperrfrist = models.CharField(max_length=30, blank=True, null=True)
    loeschfrist = models.CharField(max_length=30, blank=True, null=True)
    betroffenenKreis = models.ManyToManyField(Betroffenenkreis, blank=True, null=True,
                                              verbose_name="Kreis der Betroffenen")
    empfaenger = models.ManyToManyField(EmpfaengerPeriodizitaet, blank=True, null=True,
                                        verbose_name="Empfänger der Daten")

    def __unicode__(self):
        return self.bezeichnung


class Allgemeineangaben(models.Model):
    name = models.CharField(max_length=30)
    anschrift = models.CharField(max_length=30, blank=True)
    organisationseinheit = models.CharField(max_length=30)
    zweckbestimmung = models.CharField(max_length=255)
    verfahrenBezeichnung = models.CharField(max_length=255)
    rechtsgrundlage = models.CharField(max_length=255)

    def __unicode__(self):
        return "{}, {}".format(self.name, self.organisationseinheit)


class Massnahme(models.Model):
    BEDROHUNGEN = (
        ('VERTRAULICHKEIT', 'Vertraulichkeit'),
        ('INTEGRITAET', 'Integrität'),
        ('VERFUEGBARKEIT', 'Verfügbarkeit'),
        ('AUTHENTIZITAET', 'Authentizität'),
        ('REVISIONSFAEHIGKEIT', 'Refevisionsfähigkeit'),
        ('TRANSPARENZ', 'Transparenz')
    )
    bedrohung = models.CharField(max_length=30, choices=BEDROHUNGEN)
    bezeichnung = models.TextField()

    def __unicode__(self):
        return self.bezeichnung + " (" + self.get_bedrohung_display() + ")"


class Betriebssystem(models.Model):
    bezeichnung = models.CharField(max_length=30)

    def __unicode__(self):
        return self.bezeichnung


class Sicherheitsverfahren(models.Model):
    VERFAHRENTYP = (
    ('EINZELPLATZ', 'Einzelplatzsystem'), ('CLIENTSERVER', 'Client-Server'), ('GROSSRECHNER', 'Großrechner'))

    CLIENTS = (('TERMINAL', 'Terminal/Netz-PC'), ('PC', 'PC'))
    DATENSPEICHERUNG = (
    ('SERVER_IN', "Server innerhalb der Behörde"), ('SERVER_OUT', 'Server bei anderen Institutionen'),
    ('GROSSRECHNER', 'Großrechner'), ('PC', 'PC/Arbeitsplatzrechner'))
    KOMMUNIKATION = (('GESCHLOSSENES_NETZ','geschlossenes Netz innerhalb der Behörde (LAN)'),
                     ('NETZ_EXTERN_LEITUNG_1','Netz über externe Leitungen innerhalb eines geschlossenen Benutzerkreis - Landesverwaltungsnetz'),
                     ('NETZ_EXTERN_LEITUNG_2','Netz über externe Leitungen innerhalb eines geschlossenen Benutzerkreis - Sonstiges'),
                     ('OFFENES_NETZ', 'Offenes Netz (z.B. Internet)'),
                     ('SONSTIGES', 'Sonstige eingesetzte Hardware (z.B. Chipkarte, Kartenlesegeräte etc.)'))

    typ = models.CharField(max_length=30, choices=VERFAHRENTYP, verbose_name="Technik des Verfahrens")
    betriebssystem = models.ForeignKey(Betriebssystem, verbose_name="Betriebssystem" if typ == VERFAHRENTYP[
        0] else "Betriebsystem des Servers")
    client = models.CharField(max_length=30, choices=CLIENTS)
    datenspeicherung = models.CharField(max_length=30, choices=DATENSPEICHERUNG)
    kommunikation = models.CharField(max_length=30, choices=KOMMUNIKATION, default='GESCHLOSSENES_NETZ')


class Software(models.Model):
    bezeichnung = models.CharField(max_length=255)
    version = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.bezeichnung


class Sicherheitskonzept(models.Model):
    id = models.AutoField(primary_key=True)
    massnahmen = models.ManyToManyField(Massnahme, verbose_name="Technische und organisatorische Maßnahmen")
    verfahren = models.ForeignKey(Sicherheitsverfahren, verbose_name="Technik des Verfahrens")
    software = models.ManyToManyField(Software, verbose_name="Eingesetzte Software", blank=True, null=True)

    def __unicode__(self):
        return "{}. Konzept".format(self.id)


class Ergebnisvorabkontrolle(models.Model):
    ergebnis = models.TextField()

    def __unicode__(self):
        return self.ergebnis


class Verfahrensverzeichnis(models.Model):
    allgemeineangaben = models.ForeignKey(Allgemeineangaben, blank=True, null=True, verbose_name="Allgemeine Angaben")
    sicherheitskonzept = models.ForeignKey(Sicherheitskonzept, blank=True, null=True, verbose_name="Sicherheitskonzept")
    ergebnisvorabkontrolle = models.ForeignKey(Ergebnisvorabkontrolle, blank=True, null=True,
                                                verbose_name="Ergebnis Vorabkontrolle")
    verfahren = models.ManyToManyField(Verfahren, blank=True, null=True, verbose_name="Verfahren")

    def __unicode__(self):
        return self.allgemeineangaben.__unicode__() if self.allgemeineangaben else "{}. Verfahrensverzeichnis".format(
            self.id)


class Report(models.Model):
    verfahrensverzeichnis = models.ForeignKey(Verfahrensverzeichnis, null=False)
    MELDEARTEN = (('WESENTLICHE_AENDERUNG', "Wesentliche Änderung"),
                  ('ERSTMELDUNG', "Neues Verahren/Erstmeldung"))
    VERFAHRENSBESTIMMUNGEN = (('VERFAHREN_EINSICHTNAHME', "Das Verfahren ist zur Einsichtnahme bestimmt"),
                              ('VERFAHREN_TEILWEISE_EINSICHT',
                               "Das Verfahren ist nur teilweise zur Einsichtnahme bestimmt."),
                              ('VERFAHREN_NICHT_EINSICHT', "Das Verfahren ist nicht zur Einsichtnahme bestimmt"),
                              ('VERFAHREN_TEIL_GEMEIN_VERBUND',
                               "Das Verfahren ist Teil eines gemeinsamen oder verbundenen Verfahrens"))

    meldeart = models.CharField(choices=MELDEARTEN, max_length=30, default='ERSTMELDUNG')
    vefahrensbestimmung = models.CharField(choices=VERFAHRENSBESTIMMUNGEN, max_length=30,
                                           default='VERFAHREN_EINSICHTNAHME')

    datum = models.DateField(default=datetime.today())
