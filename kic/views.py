import logging
from typing import Any

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from .models import (
    Achievement,
    Country,
    Counsellor,
    Mission,
    Service,
    Testimonial,
    TestPreparationClass,
)

logger = logging.getLogger(__name__)


class HomeView(TemplateView):
    template_name = 'kic/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['counsellors'] = Counsellor.objects.filter(is_active=True)
        context['testimonials'] = Testimonial.objects.filter(is_featured=True)
        return context


class UniversityView(TemplateView):
    template_name = 'kic/university.html'


class TrainingView(TemplateView):
    template_name = 'kic/training.html'


class ServicesView(TemplateView):
    template_name = 'kic/services.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'kic/service_detail.html'
    context_object_name = 'service'
    slug_url_kwarg = 'service_slug'


class AboutView(TemplateView):
    template_name = 'kic/about.html'


class ContactView(TemplateView):
    template_name = 'kic/contact.html'


class CountryDetailView(DetailView):
    model = Country
    template_name = 'kic/country_detail.html'
    context_object_name = 'country'
    slug_url_kwarg = 'country_slug'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        country = self.object
        context['why_study'] = country.why_study.all()
        context['facts'] = country.facts.all()
        context['reasons'] = country.reasons.all()
        context['faqs'] = country.faqs.all()
        return context


class TestPreparationClassDetailView(DetailView):
    model = TestPreparationClass
    template_name = 'kic/test_preparation_class_detail.html'
    context_object_name = 'preparation_class'
    slug_url_kwarg = 'preparation_class_slug'
