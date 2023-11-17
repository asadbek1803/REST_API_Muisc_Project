from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=140)
    album_image = models.ImageField(blank=True, null=True, upload_to='images/album/')
    music = models.ForeignKey('song.Song', on_delete=models.CASCADE)
    album_about = models.TextField()
    author = models.ForeignKey('song.Artist', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    views = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-views', )
        db_table = "Album"
        verbose_name_plural = 'Albo\'mlar'
