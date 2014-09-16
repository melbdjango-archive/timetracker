from django.contrib import admin
from .models import Project, Client, Entry


class ProjectInline(admin.StackedInline):
    model = Project
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('client', 'name')
    list_display_links = ('name',)
    list_filter = ('client',)


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        ProjectInline,
    ]


class EntryAdmin(admin.ModelAdmin):
    readonly_fields = ('active',)
    list_display = ('title', 'active')


admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Entry, EntryAdmin)
