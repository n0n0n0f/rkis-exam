from django.urls import path, include
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.views.static import serve
from .models import Product
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
]

admin.site.register(Product)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Профиль пользователя'


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)

admin.site.register(User, UserAdmin)

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
