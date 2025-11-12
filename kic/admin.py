from django.contrib import admin

from .models import (
    Achievement,
    Country,
    Mission,
    Service,
    Testimonial,
    TestPreparationClass,
    University,
)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'icon']
    search_fields = ['title']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'flag']
    readonly_fields = ['slug']
    search_fields = ['name']


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    search_fields = ['name']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    readonly_fields = ['slug']
    search_fields = ['name']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'display_order', 'created_at', 'updated_at']
    search_fields = ['full_name']


@admin.register(TestPreparationClass)
class TestPreparationClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    readonly_fields = ['slug']
    search_fields = ['name']


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'website',
        'established_date',
        'enrollment_season',
        'ranking',
        'country',
        'status',
        'is_featured',
    ]
    readonly_fields = ['slug']
    search_fields = ['name', 'country__name']
    list_filter = ['status', 'is_featured']
