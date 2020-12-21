from django.contrib import admin

from .models import *

# Register your models here.
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'rank')

admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Category)
admin.site.register(Rank)
admin.site.register(Media)
admin.site.register(Eligibility)