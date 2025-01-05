from django.contrib import admin
from .models import Bus, User, Book, ContactMessage  # Don't forget to import ContactMessage if you want to add it

# Customizing the Bus model display in the Admin
class BusAdmin(admin.ModelAdmin):
    list_display = ('bus_name', 'source', 'dest', 'date', 'time', 'price', 'rem')  # Display specific fields
    search_fields = ('bus_name', 'source', 'dest')  # Enable search for bus_name, source, and destination
    list_filter = ('source', 'dest', 'date')  # Enable filtering by source, destination, and date
    
admin.site.register(Bus, BusAdmin)  # Register the Bus model with custom settings

# Customizing the User model display in the Admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')  # Display email and name in the admin
    search_fields = ('email', 'name')  # Enable search for email and name
    
admin.site.register(User, UserAdmin)  # Register the User model with custom settings

# Customizing the Book model display in the Admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('email', 'bus_name', 'source', 'dest', 'status', 'date', 'time', 'price', 'nos')  # Display relevant booking info
    search_fields = ('email', 'bus_name', 'status')  # Enable search for email, bus_name, and status
    list_filter = ('status', 'date')  # Enable filtering by booking status and date
    
admin.site.register(Book, BookAdmin)  # Register the Book model with custom settings

# If you want to add ContactMessage model to admin:
class ContactMessageAdmin(admin.ModelAdmin):
    # Customize how ContactMessages are displayed
    list_display = ('email', 'issue', 'created_at')

    # Enable search by email and issue
    search_fields = ('email', 'issue')

    # Enable filtering by created date
    list_filter = ('created_at',)

admin.site.register(ContactMessage, ContactMessageAdmin)
