# Generated by Django 5.0.6 on 2024-08-18 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_comment_avatar_alter_comment_coments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='desgription_az',
            field=models.TextField(null=True, verbose_name='Desgription of the blog'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='desgription_en',
            field=models.TextField(null=True, verbose_name='Desgription of the blog'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='title_az',
            field=models.CharField(max_length=255, null=True, verbose_name='Blog name'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Blog name'),
        ),
    ]
