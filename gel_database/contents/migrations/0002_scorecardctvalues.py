# Generated by Django 3.1.5 on 2021-03-14 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScorecardCtValues',
            fields=[
                ('target', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('filepath', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'scorecard CT values',
                'managed': False,
            },
        ),
    ]
