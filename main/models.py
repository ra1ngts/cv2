from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from filer.fields.image import FilerImageField


class Basic(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Создано')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Обновлено')
    )

    class Meta:
        abstract = True


class BaseModelPublished(models.Model):
    published = models.BooleanField(
        verbose_name=_('Опубликовано'),
        default=True
    )

    class Meta:
        abstract = True


phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message=_('Номер телефона должен быть в формате: "+79991234567". От 9 до 15 цифр.')
)


class Profile(Basic):
    name = models.CharField(
        max_length=30,
        help_text=_('Введите имя'),
        verbose_name=_('Имя')
    )
    lastname = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        help_text=_('Введите фамилию'),
        verbose_name=_('Фамилия')
    )
    image = FilerImageField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Изображение')
    )
    occupation = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text=_('Введите название профессии'),
        verbose_name=_('Профессия')
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('Введите информацию о себе'),
        verbose_name=_('Описание')
    )
    phone = models.CharField(
        null=True,
        blank=True,
        max_length=15,
        validators=[phone_validator],
        help_text=_('Введите номер телефона'),
        verbose_name=_('Номер телефона')
    )
    email = models.EmailField(
        null=True,
        blank=True,
        max_length=40,
        help_text=_('Введите адрес вашей электронной почты'),
        verbose_name=_('Электронная почта')
    )
    whatsapp = models.URLField(
        null=True,
        blank=True,
        max_length=500,
        help_text=_('Введите ссылку на WhatsApp'),
        verbose_name=_('WhatsApp')
    )
    telegram = models.URLField(
        null=True,
        blank=True,
        max_length=500,
        help_text=_('Введите ссылку на Telegram'),
        verbose_name=_('Telegram')
    )
    linkedin = models.URLField(
        null=True,
        blank=True,
        max_length=500,
        help_text=_('Введите ссылку на LinkedIn'),
        verbose_name=_('LinkedIn')
    )
    github = models.URLField(
        null=True,
        blank=True,
        max_length=500,
        help_text=_('Введите ссылку на GitHub'),
        verbose_name=_('GitHub')
    )
    cv = models.URLField(
        null=True,
        blank=True,
        max_length=500,
        help_text = _('Введите ссылку на резюме'),
        verbose_name=_('Ссылка на резюме')
    )

    def __str__(self):
        return self.name

    @classmethod
    def get_profile_data(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        verbose_name = _('Личная информация')
        verbose_name_plural = _('Личная информация')
