from django.contrib import admin
from django.urls import path, include
from textiles import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('learnapp.urls')),
    path('<int:id>/', views.Product_list, name='product'),
    path('add-to-cart/', views.add_to_cart_view, name='add_to_cart'),
    path('cart-success/', views.cart_success_view, name='cart_success'),
    path('admin/', admin.site.urls),
    path('cart/bill/', views.generate_bill_view, name='generate_bill')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)