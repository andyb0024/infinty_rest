# Generated by Django 3.2.4 on 2021-09-02 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Billings', '0001_initial'),
        ('Orders', '0003_delete_ordereditems'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Billings.billingprofile'),
        ),
    ]