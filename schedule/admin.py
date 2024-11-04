from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.urls import path
from django.shortcuts import redirect
from .models import CustomUser, Events, Teacher, Student # Import necessary models

# Custom User Admin Configuration
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)

# Unregister the default CustomUser if it was registered by mistake
try:
    admin.site.unregister(CustomUser)
except admin.sites.NotRegistered:
    pass

# Register CustomUser with the custom UserAdmin
admin.site.register(CustomUser, UserAdmin)

# Custom Admin Site Configuration
class MyAdminSite(admin.AdminSite):
    site_header = "My Custom Admin"
    site_title = "My Admin"
    index_title = "Welcome to My Admin"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('', self.admin_index_view),  # Redirect from the admin root
        ]
        return custom_urls + urls

    def admin_index_view(self, request):
        return redirect('admin:your_custom_user_changelist')  # Replace with the correct URL

# Create a custom admin site (optional)
admin_site = MyAdminSite(name='myadmin')
admin_site.register(CustomUser)

# Register Events model
admin.site.register(Events)

# Teacher model registration (Only register it once)
# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ('user', 'first_name', 'last_name', 'email', 'phone', 'qualification')




# from django.contrib import admin
# from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'phone', 'qualification', 'display_profile_image')

    # Method to display the profile image in the admin interface
    def display_profile_image(self, obj):
        if obj.profile_image:
            return f'<img src="{obj.profile_image.url}" width="50" height="50" />'
        return 'No Image'
    display_profile_image.allow_tags = True
    display_profile_image.short_description = 'Profile Image'

    # Add profile_image to the form fields
    fieldsets = (
        (None, {'fields': ('user', 'first_name', 'last_name', 'email', 'phone', 'qualification', 'profile_image')}),
    )


# from django.contrib import admin


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'phone', 'degree', 'display_profile_image')

    # Method to display the profile image in the admin interface
    def display_profile_image(self, obj):
        if obj.profile_image:
            return f'<img src="{obj.profile_image.url}" width="50" height="50" />'
        return 'No Image'
    display_profile_image.allow_tags = True
    display_profile_image.short_description = 'Profile Image'

    # Add profile_image and other fields to the form fields
    fieldsets = (
        (None, {'fields': ('user', 'first_name', 'last_name', 'email', 'phone', 'degree', 'department', 'address', 'birthday', 'profile_image')}),
    )



from django.contrib import admin
from .models import Dash_events

class DashEventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end', 'Type', 'created_at', 'updated_at')
    search_fields = ('title', 'Type')
    list_filter = ('start', 'end', 'Type')
    ordering = ('-created_at',)

# Register the Dash_events model
admin.site.register(Dash_events, DashEventsAdmin)


#   --------------------------------

#   Teacher Event Management

#   --------------------------------



from .models import Teacher_events

# class Teacher_eventsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'start', 'end', 'Type', 'created_at', 'updated_at')
#     search_fields = ('title', 'Type')
#     list_filter = ('start', 'end', 'Type')
#     ordering = ('-created_at',)

# # Register the Dash_events model
# admin.site.register(Teacher_events, Teacher_eventsAdmin)





from .models import Teacher_events

class Teacher_eventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end', 'type', 'created_at', 'updated_at')  # Added created_at and updated_at
    list_filter = ('start', 'end', 'type', 'created_at', 'updated_at')  # Added created_at and updated_at

    readonly_fields = ('created_at', 'updated_at')  # Make these fields read-only

admin.site.register(Teacher_events, Teacher_eventsAdmin)



# from .models import Faculty, Batch, Degree

# admin.site.register(Faculty)
# admin.site.register(Batch)
# admin.site.register(Degree)
