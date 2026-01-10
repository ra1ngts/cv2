from django.contrib import admin
from django.utils.translation import gettext_lazy as _

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
class ProfileAdmin(TabbedModelAdmin):
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
                'name',
                'lastname',
                'image',
                'occupation',
                'description'
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
        'level',
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
class ExperienceAdmin(admin.ModelAdmin):
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


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(TabbedModelAdmin):
    inlines = [ProjectImageInline]

    list_display = (
        'id',
        'order_by',
        'title',
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

    tab_main = (
        (None, {
            'fields': (
                'order_by',
                'title',
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
