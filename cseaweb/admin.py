from django.contrib import admin
from cseaweb.models import feedback

# Register your models here.

class  FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'comment',
        'email'
    )
admin.site.register(feedback, FeedbackAdmin)
