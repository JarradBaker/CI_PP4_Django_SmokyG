from django.contrib import admin
# from .models import Post, Comment
from .models import Category, Blog, Comment, Product, Booking
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['id', 'title', 'body', 'category__category_name', 'status']
    list_editable = ('status',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(Booking)


# # Sets an admin view for the Post table
# @admin.register(Post)
# class PostAdmin(SummernoteModelAdmin):
#     list_display = ('title', 'slug', 'status', 'created_on')
#     search_fields = ['title', 'content']
#     prepopulated_fields = {'slug': ('title',)}
#     list_filter = ('status', 'created_on')
#     summernote_fields = ('content')


# # Sets an admin view for the Comment table
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'post', 'created_on', 'approved')
#     list_filter = ('approved', 'created_on')
#     search_fields = ['name', 'email', 'body']
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(approved=True)
