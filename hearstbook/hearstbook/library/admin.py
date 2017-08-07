from django.contrib import admin
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'isbn', 'price', 'description')

admin.site.register( Book, BookAdmin)
