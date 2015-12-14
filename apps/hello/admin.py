from django.contrib import admin
from apps.hello.models import BIO


class AdminBIO(admin.ModelAdmin):
    pass

admin.site.register(BIO, AdminBIO)

