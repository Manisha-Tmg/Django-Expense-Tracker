from django.urls import path,include
from django.contrib import admin

# JWT login and refresh views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Custom Views
from api.views import RegisterView,ExpenseIncomeViewSet
from rest_framework.routers import DefaultRouter

# Router for viewset-based routes
router = DefaultRouter()
router.register(r'expenses', ExpenseIncomeViewSet, basename='expenses')

urlpatterns = [
    # admin panel
    path("admin/", admin.site.urls),

    # Jwt auth amd User registration endpoints
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/register/", RegisterView.as_view(), name="register"),

    # Expense APi
    path('api/', include(router.urls)),

]
