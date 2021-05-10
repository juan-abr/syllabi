from django.contrib import admin

from .models import *

# Register your models here.
class RankAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('color',)}

class CategoryAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('name',)}

class RequirementAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'rank')
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(Media)
admin.site.register(Eligibility)