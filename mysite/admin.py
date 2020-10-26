from .models import Slide
from django.contrib import admin
admin.site.site_title = 'CyberTech Systems Admin.'
admin.site.site_header = 'CyberTech Systems .'


class SlideAdmin(admin.ModelAdmin):
    fields = ['title', 'overview']


admin.site.register(Slide, SlideAdmin)
