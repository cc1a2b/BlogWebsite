from django.contrib import admin
from .models import Usern, Post, Comment, Category


admin.site.register(Usern)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
