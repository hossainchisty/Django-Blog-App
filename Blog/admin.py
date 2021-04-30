from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    prepopulated_fields = {'slug':('title',)}
    

admin.site.register(Post, PostAdmin)


'''
for admin
blog
1234
'''
# for user
# hossainchisty11
# >3?(Kj?]