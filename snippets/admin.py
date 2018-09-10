from django.contrib import admin

# Register your models here.
from snippets.models import User, Snippet

# admin.site.register(User)
admin.site.register(Snippet)