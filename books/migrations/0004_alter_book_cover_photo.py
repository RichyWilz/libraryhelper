# Generated by Django 4.0.5 on 2022-08-21 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_publication_date_alter_borrow_borrow_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]