# Generated by Django 3.0.7 on 2020-06-14 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_of_knowledge', models.TextField(blank=True, choices=[('Doctoral', 'Doctoral'), ('Masters', 'Masters'), ('Honors', 'Honors')], max_length=500)),
                ('domain_of_Knowledge', models.CharField(blank=True, choices=[('Computer Science', 'Computer Science'), ('Information Systems', 'Information Systems')], max_length=30)),
                ('type_of_paper', models.DateField(blank=True, choices=[('Proposal Paper', 'Proposal Paper'), ('Research Paper', 'Research Paper'), ('Thesis Paper', 'Thesis Paper')], null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
