# Generated by Django 3.1.3 on 2020-12-17 18:32

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SomeObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('args', picklefield.fields.PickledObjectField(editable=False)),
            ],
        ),
    ]
