from django.urls import include, path
from django.contrib import admin
# from rest_framework import routers

from knox import views as knox_views

from .views import CreateUserView, LoginView, ManageUserView, ListUserView, UpdateUserView, DeleteUserView

# router = routers.DefaultRouter()
# router.register(r'view', L)

app_name = "core"

urlpatterns = [
    # path('', include(router.urls)),
    path("create/", CreateUserView.as_view(), name="create"),
    path("view/", ListUserView.as_view(), name="view"),
    path("update/<str:username>/", UpdateUserView.as_view(), name="update"),
    path("delete/<str:username>/", DeleteUserView.as_view(), name="delete"),
    path("profile/", ManageUserView.as_view(), name="profile"),
    path("login/", LoginView.as_view(), name="knox_login"),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("logoutall/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
    path("admin/", admin.site.urls),
]
