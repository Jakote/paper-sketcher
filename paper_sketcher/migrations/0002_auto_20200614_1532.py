# Generated by Django 3.0.7 on 2020-06-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper_sketcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='domain_of_Knowledge',
            field=models.CharField(blank=True, choices=[('Computer Science', 'Computer Science'), ('Information Systems', 'Information Systems')], max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type_of_paper',
            field=models.DateField(blank=True, choices=[('Proposal Paper', 'Proposal Paper'), ('Research Paper', 'Research Paper'), ('Thesis Paper', 'Thesis Paper')], max_length=500),
        ),
    ]
