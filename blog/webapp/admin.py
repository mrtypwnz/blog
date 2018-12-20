from django.contrib import admin
from webapp.models import User, Article

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('favorites',)

admin.site.register(User, UserAdmin)
admin.site.register(Article)
