# Generated by Django 5.2.1 on 2025-05-21 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='certification_images/'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='description',
            field=models.TextField(help_text='Detailed description shown when accordion is expanded'),
        ),
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='review_profiles/')),
                ('review_text', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='content.course')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon', models.ImageField(blank=True, null=True, upload_to='training_features/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_features', to='content.course')),
            ],
        ),
    ]
