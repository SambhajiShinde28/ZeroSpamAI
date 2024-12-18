# Generated by Django 5.1.4 on 2024-12-08 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSpamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserMessage', models.TextField(default='None')),
                ('SpamProbability', models.ImageField(default=0, upload_to='')),
                ('NotSpamProbability', models.ImageField(default=0, upload_to='')),
                ('ModelPrediction', models.CharField(default='None', max_length=200)),
                ('Category', models.CharField(default='None', max_length=200)),
            ],
        ),
    ]
