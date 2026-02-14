from modeltranslation.translator import register, TranslationOptions

from .models import Profile, Experience, Project


@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = ('name', 'lastname', 'description')


@register(Experience)
class ExperienceTranslationOptions(TranslationOptions):
    fields = ('position', 'achievements')


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
