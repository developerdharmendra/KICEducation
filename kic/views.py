import logging
from typing import Any

from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .forms import ContactusForm
from .models import (
    Achievement,
    Country,
    Counsellor,
    Mission,
    Service,
    Testimonial,
    TestPreparationClass,
    University,
)

logger = logging.getLogger(__name__)


class HomeView(TemplateView):
    template_name = 'kic/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['counsellors'] = Counsellor.objects.filter(is_active=True)
        context['institutions'] = University.objects.filter(
            status=University.StatusChoices.ACTIVE, is_featured=True
        )
        context['testimonials'] = Testimonial.objects.filter(is_featured=True)
        return context


class UniversityView(TemplateView):
    template_name = 'kic/university.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['universities'] = University.objects.filter(status=University.StatusChoices.ACTIVE)
        return context


class UniversityDetailView(DetailView):
    template_name = 'kic/university_detail.html'
    context_object_name = 'university'
    slug_url_kwarg = 'university_slug'

    def get_queryset(self):
        return University.objects.filter(status=University.StatusChoices.ACTIVE)


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

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        service = self.object
        related_services = Service.objects.exclude(slug=service.slug)
        context['related_services'] = related_services
        return context


class AboutView(TemplateView):
    template_name = 'kic/about.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['achievements'] = Achievement.objects.all()[:5]
        context['missions'] = Mission.objects.all()[:3]
        return context


def contact_us(request):
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            user_email: str = form.cleaned_data.get('email')
            subject: str = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_TO_EMAIL],
                reply_to=[user_email],
            )
            email.send()
            return redirect('kic:contact')
    else:
        form = ContactusForm()
    return render(request, 'kic/contact.html', {'form': form})


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
