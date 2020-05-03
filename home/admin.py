from django.contrib import admin
from home import models


class FishAdmin(admin.ModelAdmin):
	list_display = ("name", "price", "location",)


admin.site.register(models.Fish, FishAdmin)
admin.site.register(models.Bug)
