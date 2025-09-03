from django.urls import path, include
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]


# Perbedaan urls.py pada aplikasi dan urls.py pada proyek?
# Berkas urls.py pada aplikasi mengatur rute URL spesifik untuk fitur-fitur dalam aplikasi tersebut.
# Sementara URL tingkat proyek dapat mengimpor rute URL dari berkas urls.py aplikasi-aplikasi.