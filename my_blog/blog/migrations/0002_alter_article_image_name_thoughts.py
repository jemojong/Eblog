# Generated by Django 5.0.1 on 2024-02-15 19:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_name',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.CreateModel(
            name='Thoughts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=400)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thoughts', to='blog.article')),
            ],
        ),
    ]