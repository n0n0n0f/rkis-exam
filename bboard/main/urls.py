from django.urls import path
from .views import index, user_login, register, user_logout, profile, service, product_detail, order_product
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'


urlpatterns = [
    path('', index, name='home'),
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('service/', service, name='service'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/<int:pk>/order/', order_product, name='order_product'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)