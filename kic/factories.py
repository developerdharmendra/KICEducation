import factory
from faker import Faker

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

fake = Faker()

COUNTRY_LIST = ['Australia', 'Canada', 'New Zealand', 'USA', 'UK']


class AchievementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Achievement

    title = factory.Faker('text', max_nb_chars=10)
    description = factory.Faker('paragraph', nb_sentences=10)


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country
        django_get_or_create = ('name',)

    name = factory.Iterator(COUNTRY_LIST)
    overview = factory.Faker('paragraph', nb_sentences=20)
    flag = factory.django.ImageField()


class CounsellorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Counsellor

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    phone = factory.Faker('phone_number')
    specialization = factory.Faker('text', max_nb_chars=5)
    bio = factory.Faker('sentence', nb_words=10)
    profile_picture = factory.django.ImageField()
    joined_on = factory.Faker('date')


class MissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Mission

    title = factory.Faker('text', max_nb_chars=5)
    description = factory.Faker('paragraph', nb_sentences=20)


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    name = factory.Faker('text', max_nb_chars=20)
    overview = factory.Faker('paragraph', nb_sentences=20)


class TestimonialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Testimonial

    full_name = factory.Faker('name')
    comment = factory.Faker('paragraph', nb_sentences=10)
    client_photo = factory.django.ImageField()


class TestPreparationClassFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TestPreparationClass

    name = factory.Faker('word')
    overview = factory.Faker('paragraph', nb_sentences=20)


class UniversityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = University

    name = factory.LazyAttribute(lambda _: fake.company() + ' University')
    logo = factory.django.ImageField(width=200, height=200)
    description = factory.Faker('paragraph', nb_sentences=20)
    website = factory.Faker('url')
    enrollment_season = factory.Faker('text', max_nb_chars=5)
    country = factory.SubFactory(CountryFactory)
    established_date = factory.Faker('date')
    address = factory.Faker('address')
