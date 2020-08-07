# Generated by Django 3.0.8 on 2020-08-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자'},
        ),
        migrations.AddField(
            model_name='user',
            name='useremail',
            field=models.EmailField(default='test@gmail.com', max_length=64, verbose_name='사용자이메일'),
            preserve_default=False,
        ),
    ]