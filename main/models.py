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


class BaseModelOrderby(models.Model):
    order_by = models.FloatField(verbose_name=_('Порядок'), default=1.0)

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
        help_text=_('Загрузите изображение'),
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
        unique=True,
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


class SkillCategory(Basic, BaseModelOrderby):
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text=_('Введите категорию навыка'),
        verbose_name=_('Категория навыка')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Категория навыков')
        verbose_name_plural = _('Категория навыков')


class Skill(Basic):
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name='skills',
        help_text=_('Выберите категорию навыка'),
        verbose_name=_('Категория навыка')
    )
    name = models.CharField(
        null=True,
        blank=True,
        max_length=120,
        help_text=_('Введите название навыка'),
        verbose_name=_('Название навыка')
    )
    level = models.IntegerField(
        default=100,
        help_text=_('Выберите уровень владения навыком'),
        verbose_name=_('Уровень владения навыком')
    )
    image = FilerImageField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Загрузите иконку навыка'),
        verbose_name=_('Иконка навыка')
    )

    def __str__(self):
        return f'{self.category.name}: {self.name}'

    class Meta:
        verbose_name = _('Навык')
        verbose_name_plural = _('Навыки')


class Experience(Basic, BaseModelPublished, BaseModelOrderby):
    company = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        help_text=_('Введите название компании'),
        verbose_name=_('Название компании')
    )
    company_url = models.URLField(
        null=True,
        blank=True,
        max_length=500,
        help_text=_('Введите ссылку на сайт компании'),
        verbose_name=_('Ссылка на сайт компании')
    )
    position = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text=_('Введите название своей позиции'),
        verbose_name=_('Название позиции')
    )
    start_date = models.DateField(verbose_name=_('Дата начала работы в компании'))
    end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Дата окончания работы в компании')
    )
    is_current = models.BooleanField(
        default=False,
        help_text=_('Работаете ли в компании в данный момент?'),
        verbose_name=_('Работа в данный момент')
    )
    achievements = models.TextField(
        null=True,
        blank=True,
        help_text=_('Введите свои достижения в компании'),
        verbose_name=_('Достижения в компании')
    )

    def __str__(self):
        return f'{self.company}: {self.position} - {self.is_current}'

    class Meta:
        ordering = ['-start_date']
        verbose_name = _('Опыт')
        verbose_name_plural = _('Опыт')


# class Project(Basic, BaseModelPublished, BaseModelOrderby):
#     title = models.CharField()
#     slug = models.SlugField(unique=True)
#     description = models.TextField()
#     image = FilerImageField()
#     technologies = models.ManyToManyField(Skill, related_name='projects')
#     github_url = models.URLField()
#     live_url = models.URLField()
#     order = models.PositiveIntegerField(default=0)
#
#     class Meta:
#         ordering = ['order', '-created_at']