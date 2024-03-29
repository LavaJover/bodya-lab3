from django.contrib.auth.base_user import BaseUserManager

class SystemUserManager(BaseUserManager):

    def create_user(self, email, password, name, surname, phone, **extra_fields):
        if not email:
            raise ValueError('Необходим email')
        if not name:
            raise ValueError('Необходимо имя пользователя')
        if not surname:
            raise ValueError('Необходима фамилия пользователя')
        if not phone:
            raise ValueError('Необходим номер телефона пользователя')
        if not password:
            raise ValueError('Необходим пароль пользователя')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            password=password,
            name=name,
            surname=surname,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, email, password, name, surname, phone, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser mast have is_superuser=True')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True')

        return self.create_user(email, password, name, surname, phone, **extra_fields)