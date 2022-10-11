
from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Notification(models.Model):
    title = models.CharField(max_length=100)

    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notif_detail", kwargs={"pk": self.pk})


class Complaints(models.Model):

    title = models.CharField(max_length=100)

    category = models.CharField(max_length=100)

    descritrion = models.TextField()
    image = models.ImageField(upload_to='complaints_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("comp_detail", kwargs={"pk": self.pk})

# JOB MODEL


class Jobs(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    descritrion = models.TextField()
    salary_desc = models.TextField()
    no_of_opening = models.IntegerField()
    contact_details = models.TextField()
    status = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=timezone.now)
    location = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"pk": self.pk})


# REVIEW MODEL

class Review(models.Model):

    Name = models.CharField(max_length=100)

    Desigination = models.CharField(max_length=100)

    description = models.TextField()
    image = models.ImageField(upload_to='review_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse("comp_detail", kwargs={"pk": self.pk})


class Userquery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.TextField()
