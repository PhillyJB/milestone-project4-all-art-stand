# Generated by Django 3.2.5 on 2021-07-15 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_auto_20210714_1446'),
        ('gallery', '0006_auto_20210714_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 'Poor'), (2, 'Ok'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])),
                ('art_piece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.art_pieces')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Comment Date')),
                ('text', models.TextField(verbose_name='Comment')),
                ('art_piece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.art_pieces')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.person')),
            ],
        ),
    ]