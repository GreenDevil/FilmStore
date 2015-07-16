from django.contrib import admin
from films.models import *

class FilmInline(admin.StackedInline):
    model = Comments
    extra = 1

class FilmAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'value', 'quantity']
    inlines = [FilmInline]

admin.site.register(Film, FilmAdmin)
admin.site.register(Order)


