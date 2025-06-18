from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # روابط التطبيقات الثلاثة
    path('accounts/', include('accounts.urls')),
    path('store/', include('store.urls')),
    path('', include('core.urls')),  # واجهة المستخدم (الصفحة الرئيسية وما حولها)
]
