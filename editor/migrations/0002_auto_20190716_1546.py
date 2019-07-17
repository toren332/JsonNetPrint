# Generated by Django 2.2 on 2019-07-16 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemphotovariant',
            name='bordered_image_region',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bordered_image_region', to='editor.WTLHA'),
        ),
        migrations.AlterField(
            model_name='itemphotovariant',
            name='image_region',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image_region', to='editor.WTLHA'),
        ),
    ]