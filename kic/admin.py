import logging

from django.contrib import admin
from django.db import models

from django.http import HttpRequest
from tinymce.widgets import TinyMCE
from unfold.admin import ModelAdmin, StackedInline, TabularInline
from unfold.contrib.filters.admin import (
    BooleanRadioFilter,
    ChoicesDropdownFilter,
    RelatedCheckboxFilter,
)

# fmt: off
from .models import (
    Achievement, Country, WhyStudy, CountryFact, StudyReason, Requirement,
    CostAndBudget, StepProcess, FAQ, Counsellor, Event, Mission, Service, Testimonial,
    TestPreparationClass, University,
)
# fmt: on

logger = logging.getLogger(__name__)


@admin.register(Achievement)
class AchievementAdmin(ModelAdmin):
    list_display = ['title', 'date']
    search_fields = ['title']
    show_full_result_count = False


class WhyStudyInline(TabularInline):
    model = WhyStudy
    tab = True
    max_num = 10
    extra = 0

    def get_queryset(self, request: HttpRequest) -> models.QuerySet:
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('country')
        return queryset


class StudyReasonInline(StackedInline):
    model = StudyReason
    tab = True
    max_num = 10
    extra = 0

    def get_queryset(self, request: HttpRequest) -> models.QuerySet:
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('country')
        return queryset


class CountryFactInline(TabularInline):
    model = CountryFact
    tab = True
    max_num = 10
    extra = 0

    def get_queryset(self, request: HttpRequest) -> models.QuerySet:
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('country')
        return queryset


class RequirementInline(TabularInline):
    model = Requirement
    tab = True
    max_num = 10
    extra = 0

    def get_queryset(self, request: HttpRequest) -> models.QuerySet:
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('country')
        return queryset


class CostAndBudgetInline(TabularInline):
    model = CostAndBudget
    tab = True
    max_num = 10
    extra = 0

    def get_queryset(self, request: HttpRequest) -> models.QuerySet:
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('country')
        return queryset


class StepProcessInline(StackedInline):
    model = StepProcess
    tab = True
    max_num = 10
    extra = 0

    def get_queryset(self, request: HttpRequest) -> models.QuerySet:
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('country')
        return queryset


class FAQInline(TabularInline):
    model = FAQ
    tab = True
    max_num = 10
    extra = 0

    def get_queryset(self, request: HttpRequest) -> models.QuerySet:
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('country')
        return queryset


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    inlines = [
        WhyStudyInline,
        StudyReasonInline,
        CountryFactInline,
        RequirementInline,
        CostAndBudgetInline,
        StepProcessInline,
        FAQInline,
    ]
    list_display = ['name', 'slug', 'flag']
    readonly_fields = ['slug']
    search_fields = ['name']
    show_full_result_count = False
    show_facets = admin.ShowFacets.NEVER


@admin.register(Counsellor)
class CounsellorAdmin(ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'position', 'joined_on', 'is_active']
    list_display_links = ['first_name', 'last_name']
    list_filter = [('is_active', BooleanRadioFilter)]
    list_filter_submit = True  #  add a submit button to the filter form
    fields = [
        ('first_name', 'last_name'),
        ('phone', 'position'),
        'profile_picture',
        'bio',
        'joined_on',
        'is_active',
    ]
    search_fields = ['first_name', 'last_name']
    show_full_result_count = False
    show_facets = admin.ShowFacets.NEVER


@admin.register(Event)
class EventAdmin(ModelAdmin):
    fields = [
        ('title', 'slug'),
        'description',
        'featured_image',
        ('start_datetime', 'end_datetime'),
        'status',
        'is_featured',
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    list_display = [
        'title',
        'slug',
        'start_datetime',
        'end_datetime',
        'status',
        'is_featured',
        'created_at',
        'updated_at',
    ]
    list_filter = [('is_featured', BooleanRadioFilter)]
    list_filter_submit = True  #  add a submit button to the filter form
    prepopulated_fields = {'slug': ['title']}
    search_fields = ['title']
    show_full_result_count = False
    show_facets = admin.ShowFacets.NEVER


@admin.register(Mission)
class MissionAdmin(ModelAdmin):
    list_display = ['title', 'icon_name']
    search_fields = ['name']
    show_full_result_count = False
    show_facets = admin.ShowFacets.NEVER


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ['name', 'slug', 'icon_name']
    readonly_fields = ['slug']
    search_fields = ['name']
    show_full_result_count = False
    show_facets = admin.ShowFacets.NEVER


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = [
        'full_name',
        'rating',
        'college',
        'display_order',
        'is_featured',
        'created_at',
        'updated_at',
    ]
    # TODO: Add filter by rating
    list_filter = [
        ('is_featured', BooleanRadioFilter),
    ]
    list_filter_submit = True  #  add a submit button to the filter form
    search_fields = ['full_name']
    show_full_result_count = False
    show_facets = admin.ShowFacets.NEVER


@admin.register(TestPreparationClass)
class TestPreparationClassAdmin(ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    list_display = ['name', 'slug']
    readonly_fields = ['slug']
    search_fields = ['name']
    show_full_result_count = False
    show_facets = admin.ShowFacets.NEVER


@admin.register(University)
class UniversityAdmin(ModelAdmin):
    fields = [
        'name',
        'logo',
        'description',
        ('website', 'established_date'),
        ('country', 'address', 'enrollment_season'),
        ('ranking', 'status'),
        'is_featured',
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
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
    list_filter = [
        ('country', RelatedCheckboxFilter),
        ('status', ChoicesDropdownFilter),
        ('is_featured', BooleanRadioFilter),
    ]
    list_filter_submit = True  #  add a submit button to the filter form
    readonly_fields = ['slug']
    search_fields = ['name', 'country__name']
    show_full_result_count = False
    show_facets = admin.ShowFacets.NEVER
