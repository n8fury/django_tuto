# Generated by Django 5.1.1 on 2024-10-17 10:18

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('min_bid_amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('current_bid', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='auction_images/')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
