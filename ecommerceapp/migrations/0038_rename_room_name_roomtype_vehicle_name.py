# Generated by Django 4.1.3 on 2024-02-18 17:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "ecommerceapp",
            "0037_rename_has_food_facility_roomtype_charging_capacity_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="roomtype",
            old_name="room_name",
            new_name="vehicle_name",
        ),
    ]