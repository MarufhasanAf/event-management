# Generated by Django 5.1.7 on 2025-03-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_category_alter_event_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(choices=[('DHAKA', 'Dhaka'), ('CHITTAGONG', 'Chittagong'), ('KHULNA', 'Khulna'), ('RAJSHAHI', 'Rajshahi'), ('BARISAL', 'Barisal'), ('SYLHET', 'Sylhet'), ('RANGPUR', 'Rangpur'), ('KISHOREGANJ', 'Kishoreganj'), ('MYMENSINGH', 'Mymensingh')], max_length=100),
        ),
    ]
