from django.contrib import admin
from .models import CustomUser, Mood, UserMood

admin.site.register(CustomUser)
admin.site.register(Mood)
admin.site.register(UserMood)
