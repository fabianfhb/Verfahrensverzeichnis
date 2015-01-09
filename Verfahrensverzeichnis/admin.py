# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin.sites import AdminSite
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from Verfahrensverzeichnis.forms import UserAdminAuthenticationForm

from Verfahrensverzeichnis.models import *
# Register your models here.

class UserAdmin(AdminSite):
    login_form = UserAdminAuthenticationForm
    index_template = None

    def has_permission(self, request):
        return request.user.is_active

class DataVerfahrenAdmin(ModelAdmin):
    pass

class VvAdmin(ModelAdmin):
    def response_post_save_change(self, request, obj):
        return HttpResponseRedirect(reverse('index'))
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Verfahrensverzeichnis)
admin.site.register(Allgemeineangaben)
admin.site.register(Verfahren)
admin.site.register(Betriebssystem)
admin.site.register(Sicherheitsverfahren)
admin.site.register(Inhalt)
admin.site.register(Empfaenger)
admin.site.register(EmpfaengerPeriodizitaet)
admin.site.register(Ergebnisvorabkontrolle)
admin.site.register(Gruppe)
admin.site.register(Person)
admin.site.register(Massnahme)
admin.site.register(Software)
admin.site.register(Sicherheitskonzept)
admin.site.register(Herkunft)
admin.site.register(Betroffenenkreis)

user_admin_site = UserAdmin(name="user_admin_site")

user_admin_site.register(Verfahrensverzeichnis, VvAdmin)
user_admin_site.register(Allgemeineangaben)
user_admin_site.register(Sicherheitsverfahren)
user_admin_site.register(Betriebssystem)
user_admin_site.register(Verfahren, DataVerfahrenAdmin)
user_admin_site.register(Inhalt)
user_admin_site.register(Empfaenger)
user_admin_site.register(EmpfaengerPeriodizitaet)
user_admin_site.register(Ergebnisvorabkontrolle)
user_admin_site.register(Gruppe)
user_admin_site.register(Person)
user_admin_site.register(Massnahme)
user_admin_site.register(Software)
user_admin_site.register(Sicherheitskonzept)
user_admin_site.register(Herkunft)
user_admin_site.register(Betroffenenkreis)
user_admin_site.register(Report)

