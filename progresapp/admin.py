
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


# Register your models here.

from .models import Wilayah,Balai,Satker,Ppk,Paket
# class BalaiAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     class Meta:
#         model = Balai


admin.site.register(Wilayah)
admin.site.register(Balai,ImportExportModelAdmin)
admin.site.register(Satker)
# admin.site.register(Kodeoutput)
# admin.site.register(Tag)
admin.site.register(Ppk)
admin.site.register(Paket,ImportExportModelAdmin)
#admin.site.register(Sumberdana)