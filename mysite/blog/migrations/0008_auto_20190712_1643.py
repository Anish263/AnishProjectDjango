# Generated by Django 2.0.13 on 2019-07-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_fav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fav',
            field=models.BooleanField(default=False),
        ),
    ]
