from django.contrib import admin
from .models import *
from rangefilter.filters import DateRangeFilter,DateTimeRangeFilter

class NovelAdmin(admin.ModelAdmin):
    list_display = ['itemid','title','author','pubdate','publisher','pricestandard','customerreviewrank','isbn']
    list_filter = (('pubdate',DateRangeFilter),)
    search_fields = ['title','author','publisher']
admin.site.register(Novel,NovelAdmin)

class NovelStoryAdmin(admin.ModelAdmin):
    list_display = ['itemid','title','story','review','piece']
    search_fields = ['title']
admin.site.register(NovelStory,NovelStoryAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ['cbakeywordeng','cbaalikeword','cbakeyword','cbar1','cbag1','cbab1','rgb']
    search_fields = ['cbaalikeword','cbakeywordeng','cbakeyword']
admin.site.register(Color,ColorAdmin)

class MusicAdmin(admin.ModelAdmin):
    list_display = ['year','title','singer','album_name','release_date','track_pop','singer_popularity','singer_followers','singer_genres']
    list_filter = ('year',('release_date',DateRangeFilter),) # 이상해
    search_fields = ['title','singer']
admin.site.register(Music,MusicAdmin)

class MusicLyricsAdmin(admin.ModelAdmin):
    list_display = ['year','title','singer','lyrics']
    list_filter = ('year',)
    search_fields = ['title','singer']
admin.site.register(MusicLyrics,MusicLyricsAdmin)

class MusicSingerAdmin(admin.ModelAdmin):
    list_display = ['singer_id','name','popularity','follwers','genres']
    search_fields = ['name']
admin.site.register(MusicSinger,MusicSingerAdmin)

class MusicAlbumAdmin(admin.ModelAdmin):
    list_display = ['album_id','album_name','release_date','total_tracks','track_id','track_name','track_pop','track_number','singer_name']
    search_fields = ['album_name','singer_name','track_name']
admin.site.register(MusicAlbum,MusicAlbumAdmin)
