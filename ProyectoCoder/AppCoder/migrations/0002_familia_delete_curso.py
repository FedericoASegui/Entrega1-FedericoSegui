# Generated by Django 4.1.1 on 2022-09-20 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('años', models.IntegerField()),
                ('fecha', models.DateField()),
                ('familiar', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]