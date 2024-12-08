from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Columns to display in the admin list view
    search_fields = ('name', 'email')  # Fields to enable search functionality
    list_filter = ('created_at',)  # Filters for the right sidebar in the admin
    ordering = ('-created_at',)  # Order by the most recent submissions
