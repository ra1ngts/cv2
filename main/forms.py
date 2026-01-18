from django import forms
from django.forms.widgets import EmailInput
from django.utils.translation import gettext_lazy as _

class ContactsForm(forms.Form):
    SUBJECT_CHOICES = [
        ('', _('Выберите тему')),
        ('work', _('Предложение работы')),
        ('project', _('Фриланс / Проект')),
        ('question', _('Вопрос'))
    ]

    name = forms.CharField(
        label=_('Имя'),
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': _('Ваше имя')})
    )
    subject = forms.ChoiceField(
        label=_('Тема'),
        choices=SUBJECT_CHOICES,
        required=True
    )
    message = forms.CharField(
        label=_('Сообщение'),
        widget=forms.Textarea(attrs={'placeholder': _('Ваше сообщение...'), 'rows': 5})
    )
    email = forms.EmailField(
        label=_('Электронная почта'),
        max_length=100,
        widget=EmailInput(attrs={'placeholder': _('example@example.com')})
    )