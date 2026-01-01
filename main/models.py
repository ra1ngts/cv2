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


class Information(Basic):
    name = models.CharField(
        max_length=255,
        help_text=_('Введите свое имя'),
        verbose_name=_('Имя')
    )
    lastname = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text=_('Введите фамилию'),
        verbose_name=_('Фамилия')
    )
    image = FilerImageField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Изображение')
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('Введите описание'),
        verbose_name=_('Описание')
    )
    phone = models.CharField(
        null=True,
        blank=True,
        max_length=15,
        help_text=_('Введите номер телефона'),
        verbose_name=_('Номер телефона')
    )
    email = models.EmailField(
        null=True,
        blank=True,
        max_length=40,
        help_text=_('Введите адрес вашей электронной почты'),
        verbose_name=_('Электронная почта')
    ) #TODO добавить валидатор для email

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Информация')
        verbose_name_plural = _('Информация')
