from django.contrib import admin
from .models import JournalEntry

class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'mood')
    list_filter = ('date_posted', 'mood')
    search_fields = ('title', 'content', 'tags')

admin.site.register(JournalEntry, JournalEntryAdmin)