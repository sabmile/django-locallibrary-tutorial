from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)


class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'date_of_birth',
        'date_of_death'
    )
    fields = [
        'first_name',
        'last_name',
        ('date_of_birth', 'date_of_death')
    ]
    inlines = [BooksInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = (
        'status',
        'due_back'
    )
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )


class BookInstanceInline(admin.TabularInline):
    """Defines format of inline book instance insertion (used in BookAdmin)"""
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'display_genre'
    )
    inlines = [BookInstanceInline]

