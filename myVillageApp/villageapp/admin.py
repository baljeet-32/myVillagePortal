from django.contrib import admin
from villageapp.models import Notification
from villageapp.models import Complaints, Jobs, Review, Userquery

# Register your models here.

admin.site.register(Notification)
admin.site.register(Complaints)
admin.site.register(Jobs)
admin.site.register(Review)
admin.site.register(Userquery)
