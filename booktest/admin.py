from django.contrib import admin
from .models import BookInfo,HeroInfo

# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)