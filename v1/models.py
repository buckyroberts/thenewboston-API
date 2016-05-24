from django.db import models


class ApiToken(models.Model):
    token = models.CharField(max_length=256, primary_key=True)
    access_level = models.IntegerField(default=0)
    is_master = models.BooleanField(default=False)

    def __str__(self):
        if self.is_master:
            return self.token + ' (master)'
        return self.token + ' (' + str(self.access_level) + ')'


class Major(models.Model):
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.CharField(blank=True, max_length=128)
    name = models.CharField(max_length=128)
    major = models.ForeignKey(Major, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Video(models.Model):
    episode = models.IntegerField()
    title = models.CharField(max_length=128)
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    youtube_code = models.CharField(max_length=16)

    def __str__(self):
        return self.course.name + ' - ' + str(self.episode) + ' - ' + self.title
