from django.db import models

class Artist(models.Model):
    full_name = models.CharField(max_length=140)
    artist_image = models.ImageField(blank=True, null=True, upload_to='images/artist/')
    year = models.PositiveSmallIntegerField(default=1994)
    address = models.CharField(max_length=160)
    phone = models.CharField(max_length=24, default="+998")
    email = models.EmailField(blank=True, null=True, default="@gmail.com")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "Artist"
        ordering = ("year", )
        verbose_name_plural = 'Qo\'shiqchilar'