# Generated by Django 5.1 on 2024-08-10 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(max_length=255)),
                ('nationality', models.CharField(choices=[('BR', 'Brazil'), ('US', 'United States'), ('CA', 'Canada'), ('UK', 'United Kingdom'), ('AU', 'Australia'), ('DE', 'Germany'), ('FR', 'France'), ('IT', 'Italy'), ('ES', 'Spain'), ('JP', 'Japan'), ('CN', 'China'), ('IN', 'India'), ('RU', 'Russia'), ('JP', 'Japan')], max_length=200)),
            ],
        ),
    ]
