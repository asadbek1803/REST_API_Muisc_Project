from django.db import models

class Song(models.Model):
    song_rate = (
        ('very bad', '⭐'),
        ('bad', '⭐⭐'),
        ('not bad', '⭐⭐⭐'),
        ('good', '⭐⭐⭐⭐'),
        ('very good', '⭐⭐⭐⭐⭐')
    )

    song_genre = (
        ('pop', 'Pop'),
        ('hip hop', 'Hip Hop'),
        ('rock', 'Rock'),
        ('soul', 'Soul'),
        ('country', 'Country'),
        ('folk', 'Folk'),
        ('jazz', 'Jazz'),
        ('disco', 'Disco'),
        ('classical', 'Classical'),
        ('electronic', 'Electronic'),
        ('music for children', 'Music For Children')
    )
    song_image = models.ImageField(blank=True, null=True, upload_to='images/song/')
    music = models.FileField(upload_to='music/song/')
    title = models.CharField(max_length=90)
    genre = models.CharField(max_length=50, choices=song_genre)
    artist = models.ManyToManyField('song.artist', blank=True, null=True)
    song_year = models.PositiveSmallIntegerField()
    song_rate = models.CharField(max_length=18, choices=song_rate)
    sending_date = models.DateTimeField(auto_now=True)
    song_time = models.CharField(max_length=110, default="3:14", blank=True, null=True)
    listened = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Song"
        ordering = ('song_year', )
        verbose_name_plural = "Qo'shiqlar"

