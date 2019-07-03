from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'contact_date')
    list_display_links = ('id', 'name', 'subject')
    search_fields = ('name', 'subject', 'email')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)