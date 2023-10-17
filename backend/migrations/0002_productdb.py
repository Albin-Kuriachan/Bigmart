# Generated by Django 4.2.1 on 2023-06-02 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, max_length=50, null=True)),
                ('ProductName', models.CharField(blank=True, max_length=50, null=True)),
                ('Description', models.CharField(blank=True, max_length=500, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
