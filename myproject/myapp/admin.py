from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Young_user)
admin.site.register(ELDER_user)
admin.site.register(elder_table)
admin.site.register(younger_table)
admin.site.register(Current_status_younger)
