# Generated by Django 4.2.16 on 2024-12-04 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('avatar', models.ImageField(blank=True, upload_to='media')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('friends', models.ManyToManyField(blank=True, to='service_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('winnerScore', models.IntegerField()),
                ('loserScore', models.IntegerField()),
                ('loser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loser', to='service_app.profile')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='service_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='FriendShipRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Accepted'), (2, 'Declined')], default=0)),
                ('receiver_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='service_app.profile')),
                ('sender_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='service_app.profile')),
            ],
        ),
    ]
