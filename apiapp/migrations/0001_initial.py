# Generated by Django 4.2.1 on 2023-05-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('W', 'Women'), ('M', 'Men'), ('K', 'Kids'), ('E', 'Electronics')], max_length=15)),
                ('image', models.ImageField(default='default.png', upload_to='category_images')),
            ],
        ),
    ]
