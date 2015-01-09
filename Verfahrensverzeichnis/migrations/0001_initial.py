# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allgemeineangaben',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('anschrift', models.CharField(max_length=30, blank=True)),
                ('organisationseinheit', models.CharField(max_length=30)),
                ('zweckbestimmung', models.CharField(max_length=255)),
                ('verfahrenBezeichnung', models.CharField(max_length=255)),
                ('rechtsgrundlage', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Betriebssystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bezeichnung', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Betroffenenkreis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bezeichnung', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Empfaenger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_drittstaat', models.BooleanField(default=None)),
                ('bezeichnung', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmpfaengerPeriodizitaet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('periodizitaet', models.CharField(max_length=30)),
                ('empfaenger', models.ForeignKey(to='Verfahrensverzeichnis.Empfaenger')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ergebnisvorabkontrolle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ergebnis', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gruppe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bezeichnung', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Herkunft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bezeichnung', models.CharField(max_length=255)),
                ('is_drittland', models.BooleanField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inhalt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bezeichnung', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Massnahme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bedrohung', models.CharField(max_length=30, choices=[(b'VERTRAULICHKEIT', b'Vertraulichkeit'), (b'INTEGRITAET', b'Integrit\xc3\xa4t'), (b'VERFUEGBARKEIT', b'Verf\xc3\xbcgbarkeit'), (b'AUTHENTIZITAET', b'Authentizit\xc3\xa4t'), (b'REVISIONSFAEHIGKEIT', b'Refevisionsf\xc3\xa4higkeit'), (b'TRANSPARENZ', b'Transparenz')])),
                ('bezeichnung', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('vorname', models.CharField(max_length=30)),
                ('zugriffberechtigt', models.BooleanField(default=None)),
                ('gruppen', models.ManyToManyField(to='Verfahrensverzeichnis.Gruppe', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meldeart', models.CharField(default=b'ERSTMELDUNG', max_length=30, choices=[(b'WESENTLICHE_AENDERUNG', b'Wesentliche \xc3\x84nderung'), (b'ERSTMELDUNG', b'Neues Verahren/Erstmeldung')])),
                ('vefahrensbestimmung', models.CharField(default=b'VERFAHREN_EINSICHTNAHME', max_length=30, choices=[(b'VERFAHREN_EINSICHTNAHME', b'Das Verfahren ist zur Einsichtnahme bestimmt'), (b'VERFAHREN_TEILWEISE_EINSICHT', b'Das Verfahren ist nur teilweise zur Einsichtnahme bestimmt.'), (b'VERFAHREN_NICHT_EINSICHT', b'Das Verfahren ist nicht zur Einsichtnahme bestimmt'), (b'VERFAHREN_TEIL_GEMEIN_VERBUND', b'Das Verfahren ist Teil eines gemeinsamen oder verbundenen Verfahrens')])),
                ('datum', models.DateField(default=datetime.datetime(2015, 1, 7, 18, 4, 28, 260666))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sicherheitskonzept',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('massnahmen', models.ManyToManyField(to='Verfahrensverzeichnis.Massnahme', verbose_name=b'Technische und organisatorische Ma\xc3\x9fnahmen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sicherheitsverfahren',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typ', models.CharField(max_length=30, verbose_name=b'Technik des Verfahrens', choices=[(b'EINZELPLATZ', b'Einzelplatzsystem'), (b'CLIENTSERVER', b'Client-Server'), (b'GROSSRECHNER', b'Gro\xc3\x9frechner')])),
                ('client', models.CharField(max_length=30, choices=[(b'TERMINAL', b'Terminal/Netz-PC'), (b'PC', b'PC')])),
                ('datenspeicherung', models.CharField(max_length=30, choices=[(b'SERVER_IN', b'Server innerhalb der Beh\xc3\xb6rde'), (b'SERVER_OUT', b'Server bei anderen Institutionen'), (b'GROSSRECHNER', b'Gro\xc3\x9frechner'), (b'PC', b'PC/Arbeitsplatzrechner')])),
                ('betriebssystem', models.ForeignKey(verbose_name=b'Betriebsystem des Servers', to='Verfahrensverzeichnis.Betriebssystem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bezeichnung', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Verfahren',
            fields=[
                ('lfdNr', models.AutoField(serialize=False, primary_key=True)),
                ('bezeichnung', models.CharField(max_length=255)),
                ('geschuetzt', models.BooleanField(default=None, verbose_name=b'gesch\xc3\xbctzt')),
                ('periodizitaet', models.CharField(max_length=30, null=True, verbose_name=b'Periodizit\xc3\xa4t der Daten', blank=True)),
                ('sperrfrist', models.CharField(max_length=30, null=True, blank=True)),
                ('loeschfrist', models.CharField(max_length=30, null=True, blank=True)),
                ('betroffenenKreis', models.ManyToManyField(to='Verfahrensverzeichnis.Betroffenenkreis', null=True, verbose_name=b'Kreis der Betroffenen', blank=True)),
                ('empfaenger', models.ManyToManyField(to='Verfahrensverzeichnis.EmpfaengerPeriodizitaet', null=True, verbose_name=b'Empf\xc3\xa4nger der Daten', blank=True)),
                ('gruppen', models.ManyToManyField(to='Verfahrensverzeichnis.Gruppe', null=True, verbose_name=b'Zugriffsberechtigte Gruppen', blank=True)),
                ('herkunft', models.ForeignKey(verbose_name=b'Herkunft der Daten', blank=True, to='Verfahrensverzeichnis.Herkunft', null=True)),
                ('inhalt', models.ManyToManyField(to='Verfahrensverzeichnis.Inhalt')),
                ('personen', models.ManyToManyField(to='Verfahrensverzeichnis.Person', null=True, verbose_name=b'Zugriffsberechtigte Personen', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Verfahrensverzeichnis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allgemeineangaben', models.ForeignKey(verbose_name=b'Allgemeine Angaben', blank=True, to='Verfahrensverzeichnis.Allgemeineangaben', null=True)),
                ('ergebnisvorabkontrolle', models.ForeignKey(verbose_name=b'Ergebnis Vorabkontrolle', blank=True, to='Verfahrensverzeichnis.Ergebnisvorabkontrolle', null=True)),
                ('sicherheitskonzept', models.ForeignKey(verbose_name=b'Sicherheitskonzept', blank=True, to='Verfahrensverzeichnis.Sicherheitskonzept', null=True)),
                ('verfahren', models.ManyToManyField(to='Verfahrensverzeichnis.Verfahren', null=True, verbose_name=b'Verfahren', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sicherheitskonzept',
            name='software',
            field=models.ManyToManyField(to='Verfahrensverzeichnis.Software', null=True, verbose_name=b'Eingesetzte Software', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sicherheitskonzept',
            name='verfahren',
            field=models.ForeignKey(verbose_name=b'Technik des Verfahrens', to='Verfahrensverzeichnis.Sicherheitsverfahren'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='verfahrensverzeichnis',
            field=models.ForeignKey(to='Verfahrensverzeichnis.Verfahrensverzeichnis'),
            preserve_default=True,
        ),
    ]
