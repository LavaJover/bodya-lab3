from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class SystemBackend(BaseBackend):

    def authenticate(self, request, email, password, **kwargs):
        user_model = get_user_model()
        print(user_model, email, password)
        try:
            user = user_model.objects.get(email=email)
        except user_model.DoesNotExist:
            return None

        if user.check_password(password):
            print('OK', user)
            return user
        else:
            return None

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None