from django.db import models
from datetime import datetime, timedelta

class Client(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey('Client')

    def __str__(self):
        return self.name


class Entry(models.Model):
    title = models.CharField(max_length=400)
    project = models.ForeignKey('Project', null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Entries'

    @property
    def active(self):
        return not self.end_time

    @active.setter
    def active(self, value):
        if not value and not self.end_time:
            self.end_time = datetime.now()
            self.save()

    @property
    def duration(self):
        return (end_time - start_time).minutes

    @duration.setter
    def duration(self, value):
        """Provide a value in minutes to reset duration"""
        try:
            self.end_time = self.start_time + timedelta(minutes=int(value))
            self.save()
        except ValueError:
            print 'An integer value is required'
