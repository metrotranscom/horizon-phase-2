# Generated by Django 2.1 on 2019-06-27 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20190626_0122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='call_to_action_md_cn',
        ),
        migrations.RemoveField(
            model_name='step',
            name='call_to_action_md_en',
        ),
        migrations.RemoveField(
            model_name='step',
            name='call_to_action_md_es',
        ),
        migrations.RemoveField(
            model_name='step',
            name='description_md_cn',
        ),
        migrations.RemoveField(
            model_name='step',
            name='description_md_en',
        ),
        migrations.RemoveField(
            model_name='step',
            name='description_md_es',
        ),
        migrations.RemoveField(
            model_name='step',
            name='strategy_cons_cn',
        ),
        migrations.RemoveField(
            model_name='step',
            name='strategy_cons_en',
        ),
        migrations.RemoveField(
            model_name='step',
            name='strategy_cons_es',
        ),
        migrations.RemoveField(
            model_name='step',
            name='strategy_description_cn',
        ),
        migrations.RemoveField(
            model_name='step',
            name='strategy_description_en',
        ),
        migrations.RemoveField(
            model_name='step',
            name='strategy_description_es',
        ),
        migrations.RemoveField(
            model_name='step',
            name='strategy_pros_cn',
        ),
        migrations.RemoveField(
            model_name='step',
            name='strategy_pros_en',
        ),
        migrations.RemoveField(
            model_name='step',
            name='strategy_pros_es',
        ),
        migrations.RemoveField(
            model_name='step',
            name='title_md_cn',
        ),
        migrations.RemoveField(
            model_name='step',
            name='title_md_en',
        ),
        migrations.RemoveField(
            model_name='step',
            name='title_md_es',
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_1_cn',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 1 (Chinese)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_1_en',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 1 (English)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_1_es',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 1 (Spanish)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_1_meta_description',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Public field 1 Meta Description'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_2_cn',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 2 (Chinese)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_2_en',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 2 (English)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_2_es',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 2 (Spanish)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_2_meta_description',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Public field 2 Meta Description'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_3_cn',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 3 (Chinese)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_3_en',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 3 (English)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_3_es',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 3 (Spanish)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_3_meta_description',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Public field 3 Meta Description'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_4_cn',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 4 (Chinese)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_4_en',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 4 (English)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_4_es',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 4 (Spanish)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_4_meta_description',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Public field 4 Meta Description'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_5_cn',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 5 (Chinese)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_5_en',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 5 (English)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_5_es',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 5 (Spanish)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_5_meta_description',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Public field 5 Meta Description'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_6_cn',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 6 (Chinese)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_6_en',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 6 (English)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_6_es',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 6 (Spanish)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_6_meta_description',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Public field 6 Meta Description'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_7_cn',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 7 (Chinese)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_7_en',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 7 (English)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_7_es',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 7 (Spanish)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_7_meta_description',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Public field 7 Meta Description'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_8_cn',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 8 (Chinese)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_8_en',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 8 (English)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_8_es',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Public field 8 (Spanish)'),
        ),
        migrations.AddField(
            model_name='step',
            name='public_field_8_meta_description',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Public field 8 Meta Description'),
        ),
    ]
