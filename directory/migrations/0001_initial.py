# Generated by Django 3.2.5 on 2021-07-14 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address_line_1', models.CharField(max_length=20)),
                ('post_code_1', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('account_type', models.CharField(choices=[('ART', 'Artist'), ('CUS', 'Customer')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.person')),
            ],
            bases=('directory.person',),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.person')),
            ],
            bases=('directory.person',),
        ),
    ]
