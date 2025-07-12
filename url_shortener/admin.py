from django.contrib import admin

# Register your models here.

from .models.URL import URL

class URLShortenerAdmin(admin.ModelAdmin):
    list_display = ('origin_url', 'shortened_code', 'times_used')

# Register your models here.

admin.site.register(URL, URLShortenerAdmin)
