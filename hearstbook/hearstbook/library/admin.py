from django.contrib import admin
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'isbn', 'cost', 'description')
    def cost(self, obj):
        return '$%.2f' % obj.price

admin.site.register( Book, BookAdmin)
