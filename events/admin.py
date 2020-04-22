from django.contrib import admin
from .models import Event, Registration
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

admin.site.site_header = 'Career And Counseling Cell'

# Register your models here.


class InlineRegistration(admin.TabularInline):
    model = Registration


class EventAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    inlines = [InlineRegistration]
    list_display = ('event_name', 'description', 'date', 'status',)
    list_display_links = ('event_name', 'description')
    list_editable = ('status', 'date')
    list_filter = ('date', 'status')
    search_fields = ('user', 'roll_no', 'course', 'branch')
    list_max_show_all = 50


class RegistrationAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    list_display = ('user', 'event', 'date', 'attended')
    list_display_links = ('user', 'event')
    list_editable = ('attended',)
    list_filter = ('date', 'event', 'attended')
    search_fields = ('user', 'event')


admin.site.register(Event, EventAdmin)
admin.site.register(Registration, RegistrationAdmin)
