# Generated by Django 3.1.7 on 2021-02-28 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiary',
            name='policies',
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='beneficiaries', to='account.member'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='policy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='beneficiary_policies', to='account.policy'),
            preserve_default=False,
        ),
    ]
