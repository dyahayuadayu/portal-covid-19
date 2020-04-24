from django.contrib import admin
from .models import Category, Post, Comment, PostView, Profile, Asset

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','timestamp','post')
    search_fields = ('user__username', 'timestamp','post__title')
    readonly_fields=('user', 'timestamp','content','post')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def has_add_permission(self, request):
        return False

class AssetAdmin(admin.ModelAdmin):
    list_display = ('image',)
    search_fields = ('image',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Comment, CommentAdmin)