# Generated by Django 4.0.3 on 2022-03-24 08:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usersapp', '0004_alter_user_options_alter_user_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('4d6fc822-8700-4b7d-9195-183d890d7a82'), primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=64)),
                ('repo_link', models.URLField(max_length=255)),
                ('username', models.ManyToManyField(to='usersapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_text', models.TextField(max_length=120)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TODO.project')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersapp.user')),
            ],
            options={
                'ordering': ['-date_updated'],
            },
        ),
    ]
