# Generated by Django 2.0 on 2020-01-29 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studyInformation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('kind', models.CharField(max_length=255)),
            ],
        ),
    ]