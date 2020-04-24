from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reporter.urls'))
]

admin.site.site_header = ("SIG_2 Administration")
admin.site.site_title = ("SIG Kelompok-2 2020")
