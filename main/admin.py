from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from tabbed_admin import TabbedModelAdmin

from .models import (
    Profile,
    SkillCategory,
    Skill,
    Experience,
    Project,
    ProjectImage
)


@admin.register(Profile)
class ProfileAdmin(TranslationAdmin, TabbedModelAdmin):
    list_display = (
        'id',
        'name',
        'lastname',
        'occupation',
        'phone',
        'email',
        'created_at',
        'updated_at'
    )
    list_display_links = (
        'id',
        'name'
    )

    tab_main = (
        (None, {
            'fields': (
                'name_ru', 'name_en',
                'lastname_ru', 'lastname_en',
                'image',
                'occupation',
                'description_ru', 'description_en'
            )
        }),
    )

    tab_contacts = (
        (None, {
            'fields': (
                'phone',
                'email',
                'whatsapp',
                'telegram',
                'linkedin',
                'github',
                'cv'
            )
        }),
    )

    tabs = [
        (_('Личные данные'), tab_main),
        (_('Контактные данные'), tab_contacts),
    ]

    group_fieldsets = True

    class Media:
        js = (
            'https://ajax.googleapis.com',
            'https://ajax.googleapis.com',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order_by',
        'name',
        'created_at',
        'updated_at'
    )
    list_display_links = (
        'id',
        'name'
    )
    list_filter = (
        'name',
    )
    ordering = ('order_by',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order_by',
        'category',
        'name',
        'created_at',
        'updated_at'
    )
    list_display_links = (
        'id',
        'category'
    )
    list_filter = (
        'category',
        'name'
    )
    ordering = ('order_by',)


@admin.register(Experience)
class ExperienceAdmin(TabbedModelAdmin, TranslationAdmin):
    list_display = (
        'id',
        'order_by',
        'company',
        'position',
        'is_current',
        'start_date',
        'end_date'
    )
    list_display_links = (
        'id',
        'company'
    )
    list_filter = (
        'company',
    )
    ordering = ('order_by',)
    filter_horizontal = ('skills',)

    tab_main = (
        (None, {
            'fields': (
                'order_by',
                'company',
                'company_url',
                'position_ru', 'position_en',
                'start_date',
                'end_date',
                'is_current',
                'achievements_ru', 'achievements_en'
            )
        }),
    )

    tab_skills = (
        (None, {
            'fields': (
                'skills',
            )
        }),
    )

    tabs = [
        (_('Данные о компании'), tab_main),
        (_('Технологический стек'), tab_skills),
    ]

    group_fieldsets = True

    class Media:
        js = (
            'https://ajax.googleapis.com',
            'https://ajax.googleapis.com',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(TabbedModelAdmin, TranslationAdmin):
    inlines = [ProjectImageInline]

    list_display = (
        'id',
        'order_by',
        'title',
        'description',
        'is_published'
    )
    list_display_links = (
        'id',
        'title'
    )
    list_filter = (
        'title',
        'is_published'
    )
    ordering = ('order_by',)
    filter_horizontal = ('technologies',)

    tab_main = (
        (None, {
            'fields': (
                'order_by',
                'title_ru', 'title_en',
                'description_ru', 'description_en',
                'technologies',
                'github_url',
                'live_demo_url',
                'is_published'
            )
        }),
    )

    tab_image = (
        ProjectImageInline,
    )

    tabs = [
        (_('Настройки'), tab_main),
        (_('Изображения'), tab_image),
    ]

    group_fieldsets = True

    class Media:
        js = (
            'https://ajax.googleapis.com',
            'https://ajax.googleapis.com',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
