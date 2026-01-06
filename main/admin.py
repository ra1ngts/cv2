from django.contrib import admin

from .models import (
    Profile,
    SkillCategory,
    Skill,
    Experience,
    Project
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
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
        'end_date',
    )
    list_display_links = (
        'id',
        'company'
    )
    list_filter = (
        'company',
    )
    ordering = ('order_by',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order_by',
        'title',
    )
    list_display_links = (
        'id',
        'title'
    )
    list_filter = (
        'title',
    )
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order_by',)