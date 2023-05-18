from django.contrib import admin
from django.urls import path
from main.views import CadastrosViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastros/', CadastrosViews.as_view(), name='cadastros'),
]
