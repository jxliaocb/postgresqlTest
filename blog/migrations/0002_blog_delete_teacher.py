# Generated by Django 4.2.6 on 2023-10-07 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Title')),
                ('content', models.TextField(max_length=1024, null=True, verbose_name='Content')),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]