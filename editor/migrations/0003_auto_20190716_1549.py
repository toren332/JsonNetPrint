# Generated by Django 2.2 on 2019-07-16 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0002_auto_20190716_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemphotovariant',
            name='bordered_image_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bordered_image_region', to='editor.WTLHA'),
        ),
        migrations.AlterField(
            model_name='itemphotovariant',
            name='image_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_region', to='editor.WTLHA'),
        ),
    ]
