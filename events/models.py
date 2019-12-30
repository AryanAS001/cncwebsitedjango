from django.db import models
# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    content = models.TextField(max_length=100)
    date = models.DateField()
    pic1 = models.ImageField(default=None, upload_to='static/event pics', blank=True, null=True)
    pic2 = models.ImageField(default=None, upload_to='static/event pics', blank=True, null=True)
    pic3 = models.ImageField(default=None, upload_to='static/event pics', blank=True, null=True)
    pic4 = models.ImageField(default=None, upload_to='static/event pics', blank=True, null=True)
    pic5 = models.ImageField(default=None, upload_to='static/event pics', blank=True, null=True)
    pic6 = models.ImageField(default=None, upload_to='static/event pics', blank=True, null=True)
    pic7 = models.ImageField(default=None, upload_to='static/event pics', blank=True, null=True)
    pic8 = models.ImageField(default=None, upload_to='static/event pics', blank=True, null=True)
    pic9 = models.ImageField(default=None, upload_to='static/event pics', blank=True, null=True)
    pic10 = models.ImageField(default=None, upload_to='static/event pics', blank=True, null=True)
    pic11 = models.ImageField(default=None, upload_to='static/event pics', blank=True, null=True)
    status = models.CharField(choices=(('True', 'Upcoming'), ('False', 'Happened')), max_length=10)

    def __str__(self):
        return self.event_name