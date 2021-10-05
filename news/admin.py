from django.contrib import admin
from .models import Article, Editor, Tags

# Register your models here.
admin.site.register(Article)
admin.site.register(Editor)
admin.site.register(Tags)

