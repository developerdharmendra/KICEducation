import factory
from faker import Faker

# fmt: off
from .models import (
    Achievement, Country, WhyStudy, CountryFact, StudyReason, Requirement,
    CostAndBudget, StepProcess, FAQ, Counsellor, Mission, Service, Testimonial,
    TestPreparationClass, University,
)
# fmt: on

fake = Faker()

COUNTRY_LIST = ['Australia', 'Canada', 'New Zealand', 'USA', 'UK']


class AchievementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Achievement

    title = factory.Faker('text', max_nb_chars=10)
    image = factory.django.ImageField()


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country
        django_get_or_create = ('name',)

    name = factory.Iterator(COUNTRY_LIST)
    flag = factory.django.ImageField()
    study_reason_overview = factory.Faker('paragraph', nb_sentences=10)


class WhyStudyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WhyStudy

    country = factory.SubFactory(CountryFactory)
    point = factory.Faker('sentence', nb_words=10)


class CountryFactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CountryFact

    country = factory.SubFactory(CountryFactory)
    fact = factory.Faker('sentence', nb_words=10)


class StudyReasonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StudyReason

    country = factory.SubFactory(CountryFactory)
    reason_title = factory.Faker('sentence', nb_words=10)
    reason_description = factory.Faker('paragraph', nb_sentences=10)


class RequirementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Requirement

    country = factory.SubFactory(CountryFactory)
    level = factory.Iterator(Requirement.LevelChoices.values)
    academic = factory.Faker('paragraph', nb_sentences=5)
    language = factory.Faker('paragraph', nb_sentences=5)


class CostAndBudgetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CostAndBudget

    country = factory.SubFactory(CountryFactory)
    item = factory.Iterator(CostAndBudget.BudgetItemChoice.values)
    estimated_amount = factory.Faker('pricetag')


class StepProcessFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StepProcess

    country = factory.SubFactory(CountryFactory)
    title = factory.Faker('text', max_nb_chars=5)
    description = factory.Faker('paragraph', nb_sentences=5)


class FAQFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FAQ

    country = factory.SubFactory(CountryFactory)
    question = factory.Faker('sentence', nb_words=10)
    answer = factory.Faker('paragraph', nb_sentences=10)
    is_active = factory.Faker('random_element', elements=[True, False])


class CounsellorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Counsellor

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    phone = factory.Faker('phone_number')
    position = factory.Faker('text', max_nb_chars=5)
    bio = factory.Faker('sentence', nb_words=10)
    profile_picture = factory.django.ImageField()
    joined_on = factory.Faker('date')
    is_active = factory.Faker('random_element', elements=[True, False])


class MissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Mission

    title = factory.Faker('text', max_nb_chars=5)
    description = factory.Faker('paragraph', nb_sentences=20)
    icon_name = factory.Faker('text', max_nb_chars=5)


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    name = factory.Faker('text', max_nb_chars=20)
    icon_name = factory.Faker('text', max_nb_chars=5)
    overview = factory.Faker('paragraph', nb_sentences=20)


class TestimonialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Testimonial

    full_name = factory.Faker('name')
    comment = factory.Faker('paragraph', nb_sentences=10)
    rating = factory.Faker('random_int', min=1, max=5)
    college = factory.Faker('text', max_nb_chars=5)
    client_photo = factory.django.ImageField()
    is_featured = factory.Faker('random_element', elements=[True, False])


class TestPreparationClassFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TestPreparationClass

    name = factory.Faker('word')
    logo = factory.django.ImageField()
    overview = factory.Faker('paragraph', nb_sentences=20)


class UniversityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = University

    name = factory.LazyAttribute(lambda _: fake.company() + ' University')
    logo = factory.django.ImageField(width=200, height=200)
    description = factory.Faker('paragraph', nb_sentences=20)
    website = factory.Faker('url')
    established_date = factory.Faker('date')
    address = factory.Faker('address')
    enrollment_season = factory.Faker('text', max_nb_chars=5)
    country = factory.SubFactory(CountryFactory)
    is_featured = factory.Faker('random_element', elements=[True, False])
