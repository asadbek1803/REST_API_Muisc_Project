from django.shortcuts import render, redirect
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response



from .serializers import SongSerializer, ArtistSerializer, AlbumSerializer
from .models import Song, Artist, Album
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
# Create your views here.
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer # Song Serializer
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET', 'POST'])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        song.listened += 1
        song.save()

        return redirect('/')

    @action(detail=False, methods=['GET'])
    def top(self, request):
        song = self.get_queryset()
        song = song.order_by('-listened')[:10]
        ser = SongSerializer(song,many=True)

        return Response(ser.data)





class ArtistViewSet(viewsets.ModelViewSet):


        queryset = Artist.objects.all()
        serializer_class = ArtistSerializer
        pagination_class = LimitOffsetPagination



class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET', 'POST'])
    def view(self, request, *args, **kwargs):
        album = self.get_object()
        album.views += 1
        album.save()

        return redirect('/')

