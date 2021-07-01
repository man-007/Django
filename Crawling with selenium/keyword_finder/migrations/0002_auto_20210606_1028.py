# Generated by Django 2.1.5 on 2021-06-06 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keyword_finder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('propert', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='url',
            name='meta_data_container',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='keyword_finder.info'),
        ),
    ]