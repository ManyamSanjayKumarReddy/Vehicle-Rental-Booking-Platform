# Generated by Django 4.1.11 on 2023-10-10 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "ecommerceapp",
            "0026_orders_checkin_orders_checkout_orders_member_details_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="orders", name="checkin",),
        migrations.RemoveField(model_name="orders", name="checkout",),
        migrations.RemoveField(model_name="orders", name="member_details",),
        migrations.RemoveField(model_name="orders", name="members",),
    ]