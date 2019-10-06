from django.contrib import admin

from demo.models import Book, BookNumber, Character, Author


# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ["title", "description"]
    list_display = ["title", "description"]
    list_filter = ["published"]
    search_fields = ["title", "description"]


admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)
