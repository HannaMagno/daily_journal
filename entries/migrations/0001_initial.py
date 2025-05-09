# Generated by Django 5.2 on 2025-04-14 15:33

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('mood', models.CharField(choices=[('😊', 'Happy'), ('😢', 'Sad'), ('😠', 'Angry'), ('😲', 'Surprised'), ('😴', 'Tired'), ('😃', 'Excited'), ('😌', 'Peaceful')], default='😊', max_length=2)),
                ('tags', models.CharField(blank=True, max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Journal Entries',
                'ordering': ['-date_posted'],
            },
        ),
    ]
