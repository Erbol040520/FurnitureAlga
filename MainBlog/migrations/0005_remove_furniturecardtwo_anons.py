# Generated by Django 3.0.8 on 2020-10-12 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainBlog', '0004_furniturecardtwo_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furniturecardtwo',
            name='anons',
        ),
    ]