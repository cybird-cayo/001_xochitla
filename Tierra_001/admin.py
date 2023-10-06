from django.contrib import admin
from .models import foto


class fotoAd(admin.ModelAdmin):
    pass


admin.site.register(foto, fotoAd)
