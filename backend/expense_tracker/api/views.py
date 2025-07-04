from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, permissions
from .models import ExpenseIncome
from .serializers import ExpenseIncomeSerializer
from rest_framework.permissions import IsAuthenticated


# Registration Viewset
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Custom permission to allow users to see only their own data unless they are superusers
class IsOwnerOrSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow superusers to access everything
        if request.user.is_superuser:
            return True
        # Otherwise, only allow access to the user's own records
        return obj.user == request.user


class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperUser]

    def get_queryset(self):
        # Superusers can see all records
        if self.request.user.is_superuser:
            return ExpenseIncome.objects.all()
        # Regular users see only their own records
        return ExpenseIncome.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the logged-in user to the record
        serializer.save(user=self.request.user)