from django.urls import path, include
from django.contrib import admin

app_name = "core"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("autenticacion.urls")),
    path("backoffice/", include("backoffice.urls")),
    path("oftrabajo/", include("oficina_trabajo.urls")),
]
