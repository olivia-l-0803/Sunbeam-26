from django.contrib import admin
from .models import *  # Import your model

admin.site.register(user)
admin.site.register(forumpost)
admin.site.register(todotask)

