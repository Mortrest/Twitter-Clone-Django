# Generated by Django 3.1.1 on 2020-10-05 10:33

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
                ('username', models.CharField(blank=True, max_length=400, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('likeList', models.TextField(default='0x')),
                ('followList', models.TextField(default='0@')),
                ('followers', models.IntegerField(default=0)),
                ('followings', models.IntegerField(default=0)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(null=True)),
                ('likesCount', models.IntegerField(default=0)),
                ('commentsCount', models.IntegerField(default=0)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='accounts.profile')),
                ('user', models.ManyToManyField(to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('datePublished', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.post')),
            ],
            options={
                'ordering': ['-datePublished'],
            },
        ),
    ]
