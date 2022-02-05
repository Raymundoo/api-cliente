# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api.models import RaynhardtJWT

# Register your models here.


class RaynhardtJWTAdmin(admin.ModelAdmin):
    model = RaynhardtJWT
admin.site.register(RaynhardtJWT, RaynhardtJWTAdmin)