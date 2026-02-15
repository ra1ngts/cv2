from django.utils.translation import gettext as _  # gettext_lazy as _


def getTranslateDict():
    TranslateDict = {
        'app': {
            'sectionTitle': {
                'about': _('ОБО МНЕ'),
                'experience': _('ОПЫТ'),
                'projects': _('ПРОЕКТЫ'),
                'contact': _('КОНТАКТЫ')
            },
            'copyright': _('Давид Хурцидзе. Все права защищены.')
        },
        'profile': {
            'technologies': _('Технологии'),
            'frontend': _('Фронтенд'),
            'backend': _('Бэкенд'),
            'info': _('Список навыков пуст')
        },
        'experience': {
            'info': _('Нет доступных записей')
        },
        'contact': {
            'errors': {
                'name': _('Введите ваше имя'),
                'email': _('Введите корректный email'),
                'subject': _('Укажите тему'),
                'message': _('Введите текст сообщения')
            },
            'post': {
                'success': _('Сообщение успешно отправлено!'),
                'sending': _('Отправляем...'),
                'submit': _('Отправить')
            }
        },
        'utils': {
            'present': _('по настоящее время')
        }
    }

    return TranslateDict
