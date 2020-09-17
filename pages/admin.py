from django.contrib import admin

from .models import Contact1
# Register your models here.


class Contact1Admin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'mobile_number', 'email_id',
                    'Blood_type', 'City', 'Sample_text', 'date_day', 'gender', 'is_verified')


admin.site.register(Contact1, Contact1Admin)
