# Generated by Django 3.0.2 on 2020-08-19 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='post_pics')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
    ]