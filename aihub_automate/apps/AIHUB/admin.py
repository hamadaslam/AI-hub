from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from apps.AIHUB.models import User , CompanyInformation, projectinfoPI, workPlan, teamexperts

class StudentAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ( 'email','accountType')
    search_fields = ('email','accountType','first_name','last_name')

    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'Contact', 'accountType', 'mailingAddress' )}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
        }),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'email', 'password1', 'password2', 'first_name', 'last_name', 'Contact', 'accountType', 'mailingAddress' ),
            
        }),
       (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
        }), 
    )
   
admin.site.register(User,StudentAdmin)

admin.site.register(CompanyInformation)

admin.site.register(projectinfoPI)
admin.site.register(workPlan)
admin.site.register(teamexperts)
