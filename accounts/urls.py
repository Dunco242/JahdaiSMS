from django.urls import path
from .views import login_view, logout_view  # Import your custom view

app_name = "accounts"
urlpatterns = [
    path('accounts/login/', login_view, name="login"),
    path('accounts/logout/', logout_view, name="logout"),  # Use your custom view
]
