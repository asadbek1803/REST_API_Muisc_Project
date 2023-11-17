from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Song, Artist, Album

# Register your models here.
@admin.register(Song)
class SongRegister(ModelAdmin):
    list_display = ('title', 'music', 'genre', 'song_year', 'listened')
    list_filter = ('listened', 'genre')
    list_editable = ('genre', 'song_year')
    search_fields = ('title', 'genre')

@admin.register(Artist)
class AdminRegister(ModelAdmin):
    list_display = ('full_name', 'year', 'address', 'phone', 'email', 'is_active')
    list_filter = ('is_active', 'year')
    list_editable = ('address', 'phone', 'email')
    search_fields = ("full_name", 'email')

@admin.register(Album)
class AlbumRegister(ModelAdmin):
    list_display = ('title', 'album_about', 'created_date', 'is_active', 'views')
    list_filter = ('is_active', 'created_date', 'views')
    list_editable = ('is_active', )
    search_fields = ('title', )
