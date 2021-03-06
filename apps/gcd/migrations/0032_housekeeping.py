# Generated by Django 2.2.12 on 2020-11-12 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gcd', '0031_storycredit_signature'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creator',
            options={'ordering': ('sort_name', 'created'), 'verbose_name_plural': 'Creators'},
        ),
        migrations.AlterModelOptions(
            name='creatormembership',
            options={'ordering': ('membership_type', 'organization_name'), 'verbose_name_plural': 'Creator Memberships'},
        ),
        migrations.AlterModelOptions(
            name='creatorschool',
            options={'ordering': ('creator__sort_name', 'school_year_began', 'school_year_ended'), 'verbose_name_plural': 'Creator Schools'},
        ),
    ]
