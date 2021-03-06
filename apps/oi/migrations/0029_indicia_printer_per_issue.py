# Generated by Django 2.2.12 on 2020-06-11 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcd', '0030_indicia_printer_per_issue'),
        ('oi', '0028_creatorsignaturerevision'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='changesetcomment',
            options={'get_latest_by': 'created', 'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='issuerevision',
            name='indicia_printer',
            field=models.ManyToManyField(blank=True, related_name='issue_revisions', to='gcd.IndiciaPrinter'),
        ),
        migrations.AddField(
            model_name='issuerevision',
            name='no_indicia_printer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='seriesrevision',
            name='has_indicia_printer',
            field=models.BooleanField(default=False),
        ),
    ]
