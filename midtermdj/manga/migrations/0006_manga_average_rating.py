# Generated by Django 5.0.6 on 2024-05-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0005_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
    ]