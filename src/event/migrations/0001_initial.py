# Generated by Django 4.0.4 on 2022-05-02 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contract', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Event status',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('attendees', models.IntegerField(default=0)),
                ('notes', models.TextField(blank=True, max_length=255)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='contract.contract')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_status', to='event.eventstatus')),
                ('support_contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='support_contact', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]