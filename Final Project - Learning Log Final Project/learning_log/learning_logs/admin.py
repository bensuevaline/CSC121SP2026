from django.contrib import admin
from .models import Topic, Entry

# Register models in admin panel
admin.site.register(Topic)
admin.site.register(Entry)
