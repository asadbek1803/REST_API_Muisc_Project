from rest_framework import serializers
from song.models import *

############Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'full_name', 'artist_image', 'year', 'address', 'phone', 'email', 'is_active')




############## #End Artist
################Song
class ArtistForSong(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'full_name', 'year')


class SongSerializer(serializers.ModelSerializer):
    artist = ArtistForSong(many=True)

    class Meta:
        model = Song
        fields = ('id', 'song_image', 'music', 'title', 'genre', 'artist', 'song_year', 'song_rate', 'sending_date', 'song_time', 'listened')






########################## EndSong

###############Album
class SongForAlbum(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'music')
class AuthorForAlbum(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'full_name')

class AlbumSerializer(serializers.ModelSerializer):
    music = SongForAlbum()
    author = AuthorForAlbum()
    class Meta:
        model = Album
        fields = ('id', 'title', 'album_image', 'music', 'album_about', 'author', 'created_date', 'is_active', 'views')


###################End Album