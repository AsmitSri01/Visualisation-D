from django.contrib import admin
from . models import Dashboard_data
# Register your models here.
@admin.register(Dashboard_data)
class Admin(admin.ModelAdmin):
    list_display = [
        'end_year',
        'intensity',
        'sector',
        'topic',
        'insight',
        'url',
        'region',
        'start_year',
        'impact',
        'added',
        'published',
        'country',
        'relevance',
        'pestle',
        'source',
        'title',
        'likelihood'
    ]

    list_per_page = 50

