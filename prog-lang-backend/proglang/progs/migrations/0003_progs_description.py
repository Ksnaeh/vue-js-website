# Generated by Django 3.1.2 on 2020-10-31 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progs', '0002_review_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='progs',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]