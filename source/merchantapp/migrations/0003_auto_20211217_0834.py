# Generated by Django 3.2 on 2021-12-17 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('merchantapp', '0002_auto_20211216_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='description',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userreward',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reward', to=settings.AUTH_USER_MODEL),
        ),
    ]