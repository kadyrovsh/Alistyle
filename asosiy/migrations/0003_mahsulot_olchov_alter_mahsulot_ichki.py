# Generated by Django 4.0.6 on 2022-07-26 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0002_alter_ichki_bolim'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsulot',
            name='olchov',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='ichki',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ichki_mahsulotlari', to='asosiy.ichki'),
        ),
    ]
