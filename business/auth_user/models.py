import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.category_employee.models import CategoryEmployee


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHO0ICE = (
        ('male', 'male'),
        ('female', 'female'),
    )

    REGION_CHOICE = (
        ('Tashkent', 'Tashkent'),
        ('Tashkent region', 'Tashkent region'),
        ('Andijan', 'Andijan'),
        ('Bukhara', 'Bukhara'),
        ('Fergana', 'Fergana'),
        ('Jizzakh', 'Jizzakh'),
        ('Xorazm', 'Xorazm'),
        ('Namangan', 'Namangan'),
        ('Navoiy', 'Navoiy'),
        ('Qashqadaryo', 'Qashqadaryo'),
        ('Samarkand', 'Samarkand'),
        ('Sirdaryo', 'Sirdaryo'),
        ('Surxondaryo', 'Surxondaryo'),
    )

    objects = UserManager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    firstname = models.CharField(
        _("first name"),
        max_length=150,
        blank=True,
        null=True
    )
    lastname = models.CharField(
        _("last name"),
        max_length=150,
        blank=True,
        null=True
    )
    profile_image = models.ImageField(
        upload_to='profile_images/',
        max_length=255,
        blank=True,
        null=True
    )
    email = models.EmailField(
        _("email address"),
        blank=True
    )
    username = models.CharField(
        _('username'),
        max_length=100,
        unique=True,
        help_text=_('Required. 100 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
        null=True, blank=True
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting account."
        ), null=True, blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHO0ICE,
        null=True,
        blank=True
    )

    region = models.CharField(
        max_length=50,
        choices=REGION_CHOICE,
        null=True,
        blank=True
    )

    phone = models.PositiveBigIntegerField(
        null=True,
        blank=True
    )

    passport = models.ImageField(
        upload_to='passports/',
        null=True,
        blank=True
    )

    category_employee = models.ForeignKey(CategoryEmployee, on_delete=models.CASCADE, blank=True, null=True),

    date_joined = models.DateTimeField(
        _("date joined"),
        auto_now=True,
        null=True, blank=True
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"

    class Meta:
        db_table = 'user'
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ['id']

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    @property
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.firstname, self.lastname)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.firstname

    def update_profile(self, validated_data):
        self.firstname = validated_data.get("first_name", self.firstname)
        self.lastname = validated_data.get("last_name", self.lastname)
        self.profile_image = validated_data.get(
            "profile_image", self.profile_image
        )
        self.email = validated_data.get("email", self.email)
        self.save()
        return self

    def __str__(self):
        return f"{self.username}"

    @property
    def photo_url(self):
        try:
            return self.profile_image.url
        except Exception as e:
            print(e)
            return ''
