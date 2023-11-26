from django.contrib.auth.backends import ModelBackend
from .models import Accounts

class CustomBackend(ModelBackend):
    def authenticate(self, request, login=None, password=None, **kwargs):
        try:
            user = Accounts.objects.get(accountemail=login)
            if user.check_password(password):
                return user
        except Accounts.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Accounts.objects.get(accountid=user_id)
        except Accounts.DoesNotExist:
            return None
