from django.contrib import admin

# Register your models here.
from .forms import db_form
from .models import db

class dbAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "timestamp", "updated"]
    form = db_form

admin.site.register(db, dbAdmin)
