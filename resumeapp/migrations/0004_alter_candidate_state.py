# Generated by Django 4.1.1 on 2023-09-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0003_remove_candidate_locality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='state',
            field=models.CharField(choices=[('Koshi', 'Koshi'), ('Madhesh', 'Madhesh'), ('Bagmati', 'Bagmati'), ('Gandaki', 'Gandaki'), ('Lumbini', 'Lumbini'), ('Karnali', 'Karnali'), ('Sudurpashchim', 'Sudurpashchim')], max_length=80),
        ),
    ]
