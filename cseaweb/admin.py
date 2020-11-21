from django.contrib import admin
from cseaweb.models import feedback

# Register your models here.

class TestAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'comment',
        'email'
    )
admin.site.register(feedback, TestAdmin)
