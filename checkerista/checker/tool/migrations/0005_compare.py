# Generated by Django 3.0.8 on 2020-08-03 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0004_remove_text_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='compare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comparison', models.TextField()),
            ],
        ),
    ]