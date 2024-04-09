from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
from apps.users.models import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=False,
    )
    password = models.CharField(
        _('password'),
        max_length=100,
        blank=False,
    )
    first_name = models.CharField(
        _('first name'),
        max_length=30,
        blank=True,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=150,
        blank=True,
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into '
            'this admin site.'
        ),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be '
            'treated as active. Unselect this instead '
            'of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(
        _('date joined'),
        auto_now_add=True,
        blank=True,
    )
    photo = models.ImageField(
        db_column='photo',
        upload_to='users/%Y/%m/%d',
        blank=True,
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
