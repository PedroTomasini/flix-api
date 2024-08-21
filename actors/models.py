from django.db import models


NATIONALITY_CHOICES = (
    ('BR', 'Brazil'),
    ('US', 'United States'),
    ('CA', 'Canada'),
    ('UK', 'United Kingdom'),
    ('AU', 'Australia'),
    ('DE', 'Germany'),
    ('FR', 'France'),
    ('IT', 'Italy'),
    ('ES', 'Spain'),
    ('JP', 'Japan'),
    ('CN', 'China'),
    ('IN', 'India'),
    ('RU', 'Russia'),
    ('JP', 'Japan'),
)

class Actor(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=255)
    nationality = models.CharField(max_length=200, choices=NATIONALITY_CHOICES)

    def __str__(self):
        return self.name

