# Generated by Django 3.1.7 on 2021-03-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210321_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='groups',
        ),
        migrations.AddField(
            model_name='group',
            name='teachers',
            field=models.ManyToManyField(to='core.Teacher'),
        ),
    ]
