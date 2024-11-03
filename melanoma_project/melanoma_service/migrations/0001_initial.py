# Generated by Django 5.1.2 on 2024-10-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MelanomaImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='melanoma_images/')),
                ('is_malignant', models.BooleanField(null=True)),
                ('probability', models.FloatField(null=True)),
            ],
        ),
    ]