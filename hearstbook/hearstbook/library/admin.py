from django.contrib import admin
from .models import Book, Library


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'isbn', 'price', 'description')

admin.site.register(Book, BookAdmin)
admin.site.register(Library)
