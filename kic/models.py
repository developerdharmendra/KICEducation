from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.functions import Lower
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    flag = models.ImageField(upload_to='countries/')
    study_reason_overview = models.TextField(help_text='Overview for reason to study in a country.')
    image_1 = models.ImageField(
        upload_to='countries/',
        blank=True,
        null=True,
        help_text='Optional image for why study section.',
    )
    image_2 = models.ImageField(
        upload_to='countries/',
        blank=True,
        null=True,
        help_text='Optional image for reasons to study section.',
    )

    class Meta:
        verbose_name_plural = 'countries'
        constraints = [
            models.UniqueConstraint(Lower('name'), 'name', name='unique_lower_name_country'),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('kic:country_detail', kwargs={'country_slug': self.slug})


class WhyStudy(models.Model):
    """Model representing why student might choose to study in a country."""

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='why_study')
    point = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['country', 'point'], name='unique_country_point'),
    #     ]

    def __str__(self):
        return f'{self.country.name} - {self.point}'


class CountryFact(models.Model):
    """Model representing facts of a country."""

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='facts')
    fact = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['country', 'fact'], name='unique_country_fact', violation_error_message='Country with this fact already exists.'),
    #     ]

    def __str__(self):
        return f'Facts about {self.country.name}'


class StudyReason(models.Model):
    """Model representing study reasons of a country."""

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='reasons')
    reason_title = models.CharField(max_length=255)
    reason_description = models.TextField(max_length=500)
    position = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.country.name} - {self.reason_title}'


class Requirement(models.Model):
    """Model representing requirements to study in a country."""

    class LevelChoices(models.TextChoices):
        DIPLOMA = 'DIPLOMA', 'Diploma'
        BACHELOR = 'BACHELOR', 'Bachelor'
        MASTER = 'MASTER', 'Master'
        PHD = 'PhD', 'PhD'

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='requirements')
    level = models.CharField(max_length=20, choices=LevelChoices.choices)
    academic = models.CharField(
        max_length=150, help_text='Academic requirements such as minimum GPA, prior degree, etc.'
    )
    language = models.CharField(
        max_length=150, help_text='Language test requirements (IELTS, PTE, TOEFL, etc.).'
    )

    def __str__(self):
        return f'Study requirement for {self.country.name}'


class CostAndBudget(models.Model):
    """Model representing estimated costs and budget to study in a country."""

    class BudgetItemChoice(models.TextChoices):
        TUITION = 'TUITION', 'Tuition (per year)'
        VISA = 'VISA', 'Visa application fee'

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='budgets')
    item = models.CharField(max_length=30, choices=BudgetItemChoice.choices)
    estimated_amount = models.CharField(max_length=100)

    def __str__(self):
        return f'Estimated cost & budget for {self.country.name}'


class StepProcess(models.Model):
    """Model representing step by step process to study in a country."""

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='processes')
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    order = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'processes'
        ordering = ['order', '-created_at']

    def __str__(self):
        return f'Step by step process for {self.country.name}'


class FAQ(models.Model):
    """Model representing frequently asked questions of a country."""

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=255)
    position = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['position', '-created_at']

    def __str__(self):
        return f'{self.country.name} - {self.question}'


class University(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', 'Active Partner'
        INACTIVE = 'inactive', 'No Current Partnership'
        POTENTIAL = 'potential', 'Potential Partner'

    name = models.CharField(max_length=255, help_text='Official name of the university.')
    slug = models.SlugField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='university_logos/')
    description = models.TextField(help_text='Description of the university.')
    website = models.URLField()
    established_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=150, blank=True, null=False, default='')
    enrollment_season = models.CharField(max_length=150, help_text='e.g. January and September')
    ranking = models.PositiveIntegerField(
        blank=True, null=True, help_text='World or national ranking if available.'
    )
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='universities')
    status = models.CharField(
        max_length=20, choices=StatusChoices.choices, default=StatusChoices.ACTIVE, db_index=True
    )
    is_featured = models.BooleanField(default=False, db_index=True)

    class Meta:
        verbose_name_plural = 'universities'

    def __str__(self):
        return f'{self.name} ({self.country.name})'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('kic:university_detail', kwargs={'university_slug': self.slug})


class TestPreparationClass(models.Model):
    """Model representing test preparation classes provided by consultancy."""

    name = models.CharField(max_length=100, unique=True, help_text='e.g. IELTS, PTE')
    slug = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='preparation_classes/')
    overview = models.TextField(help_text='Overview of this test preparation class.')

    def __str__(self):
        return f'{self.name} Preparation Classes'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('kic:preparation_class_detail', kwargs={'preparation_class_slug': self.slug})


class Service(models.Model):
    """Model representing services provided by consultancy."""

    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    icon_name = models.CharField(max_length=20, help_text='e.g., user, home, settings')
    overview = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('kic:service_detail', kwargs={'service_slug': self.slug})


class Mission(models.Model):
    """Model representing consultancy missions."""

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    icon_name = models.CharField(max_length=20, help_text='e.g., user, home, settings')

    def __str__(self):
        return self.title


class Achievement(models.Model):
    """Model representing consultancy achievements."""

    title = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='achievements/')

    def __str__(self):
        return self.title


class Counsellor(models.Model):
    # REVIEW: counsellor might not be user of the system?
    # user = models.OneToOneField(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     help_text='System user account linked to this counsellor.',
    # )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    position = models.CharField(max_length=100, help_text='Position in the consultancy')
    bio = models.TextField(max_length=1000)
    profile_picture = models.ImageField(upload_to='counsellors/')
    joined_on = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self._meta.model_name} - {self.get_full_name()}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Testimonial(models.Model):
    """Model representing client testimonials for a consultancy."""

    full_name = models.CharField(max_length=120)
    comment = models.TextField(max_length=2000)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    college = models.CharField(max_length=255)
    client_photo = models.ImageField(upload_to='testimonials/')
    display_order = models.PositiveIntegerField(
        default=0, help_text='Order in which testimonial appears.'
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', '-created_at']

    def __str__(self):
        return f'{self._meta.model_name} by {self.full_name}'
