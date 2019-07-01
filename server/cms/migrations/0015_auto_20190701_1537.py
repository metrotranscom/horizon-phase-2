# Generated by Django 2.1 on 2019-07-01 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20190701_0132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='strategychoice',
            old_name='date_created',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='surveyresponse',
            old_name='date_created',
            new_name='date_updated',
        ),
        migrations.AddField(
            model_name='strategychoice',
            name='origin_step',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='cms.Step'),
            preserve_default=False,
        ),
    ]