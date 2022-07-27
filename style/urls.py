from django.contrib import admin
from django.urls import path
from asosiy.views import *
from userapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index2View.as_view()),
    path('home/', IndexView.as_view()),
    path('ichkilar/<int:pk>/', IchkiView.as_view()),
    path('ichki/<int:pk>/', MahsulotlarView.as_view()),
    path('mahsulot/<int:pk>/', MahsulotView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view()),
    path('bolimlar/', BolimlarView.as_view()),
    path('tanlangan/', TanlanganView.as_view()),
    path('savat/', SavatView.as_view()),
    path('buyurtma/', BuyurtmaView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
