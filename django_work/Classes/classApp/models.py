from django.db import models


# Create your models here.
class djangoClasses(models.Model):
    title = models.CharField(max_length=50, default='', blank=True, null=False)
    course_number = models.IntegerField(max_length=10000, default='', blank=True, null=False)
    instructor_name = models.CharField(max_length=50, default='', blank=True, null=False)
    duration = models.FloatField(default=0, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
