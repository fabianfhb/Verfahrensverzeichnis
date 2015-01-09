# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Verfahrensverzeichnis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sicherheitsverfahren',
            name='kommunikation',
            field=models.CharField(default=b'GESCHLOSSENES_NETZ', max_length=30, choices=[(b'GESCHLOSSENES_NETZ', b'geschlossenes Netz innerhalb der Beh\xc3\xb6rde (LAN)'), (b'NETZ_EXTERN_LEITUNG_1', b'Netz \xc3\xbcber externe Leitungen innerhalb eines geschlossenen Benutzerkreis - Landesverwaltungsnetz'), (b'NETZ_EXTERN_LEITUNG_2', b'Netz \xc3\xbcber externe Leitungen innerhalb eines geschlossenen Benutzerkreis - Sonstiges'), (b'OFFENES_NETZ', b'Offenes Netz (z.B. Internet)'), (b'SONSTIGES', b'Sonstige eingesetzte Hardware (z.B. Chipkarte, Kartenleseger\xc3\xa4te etc.)')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='datum',
            field=models.DateField(default=datetime.datetime(2015, 1, 8, 9, 31, 57, 256699)),
            preserve_default=True,
        ),
    ]
