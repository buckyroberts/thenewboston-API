from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    category = models.CharField(blank=True, max_length=128)
    name = models.CharField(max_length=128)
    subject = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Video(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=128)
    number = models.IntegerField()
    playlist = models.ForeignKey(Playlist, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.playlist.name + ' - ' + str(self.number) + ' - ' + self.name
