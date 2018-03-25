from django.contrib import admin
from blog_post.models import Post
from blog_post.models import ReadList
from blog_post.models import WatchList

# Register your models here.
admin.site.register(Post)
admin.site.register(ReadList)
admin.site.register(WatchList)