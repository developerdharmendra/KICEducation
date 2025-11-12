from django.conf import settings
from django.db import models
from django.db.models.functions import Lower
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    flag = models.ImageField(upload_to='flags/', blank=True, null=True)
    overview = models.TextField(help_text='Overview of why this country is ideal for students.')

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


class University(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', 'Active Partner'
        INACTIVE = 'inactive', 'No Current Partnership'
        POTENTIAL = 'potential', 'Potential Partner'

    name = models.CharField(max_length=255, help_text='Official name of the university.')
    slug = models.SlugField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='university_logos/')
    description = models.TextField(help_text='Description of the university.')
    website = models.URLField(blank=True, null=True)
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
    image = models.ImageField(upload_to='services/', null=True, blank=True)
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
    description = models.TextField()
    image = models.ImageField(upload_to='missions/', blank=True, null=True)

    def __str__(self):
        return self.title


class Achievement(models.Model):
    """Model representing consultancy achievements."""

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=False)
    date = models.DateField(blank=True, null=True)
    icon = models.ImageField(upload_to='achievements/', blank=True, null=True)

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
    specialization = models.CharField(max_length=100, help_text='Area of expertise')
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='counsellors/')
    joined_on = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self._meta.model_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Testimonial(models.Model):
    """Model representing client testimonials for a consultancy."""

    full_name = models.CharField(max_length=120)
    comment = models.TextField(max_length=2000)
    client_photo = models.ImageField(upload_to='testimonials/')
    display_order = models.PositiveIntegerField(
        default=0, help_text='Order in which testimonial appears.'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', '-created_at']

    def __str__(self):
        return f'{self._meta.model_name} by {self.full_name}'
