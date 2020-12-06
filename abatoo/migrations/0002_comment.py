# Generated by Django 3.1.3 on 2020-11-30 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abatoo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=80)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='abatoo.region')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]