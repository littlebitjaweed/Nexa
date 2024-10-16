# Generated by Django 5.1.1 on 2024-10-12 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexapp', '0013_alter_college_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='college',
            name='intake',
            field=models.FloatField(default=60),
        ),
        migrations.AlterField(
            model_name='college',
            name='pincode',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='college',
            name='specialization',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
