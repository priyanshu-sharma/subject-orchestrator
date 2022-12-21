# Generated by Django 4.0.8 on 2022-12-21 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_domain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('install_ts', models.DateTimeField(auto_now_add=True)),
                ('update_ts', models.DateTimeField(auto_now=True)),
                ('created_by_id', models.IntegerField(blank=True, null=True)),
                ('updated_by_id', models.IntegerField(blank=True, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('meta', models.JSONField(default=dict)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'so_department',
            },
        ),
        migrations.RemoveIndex(
            model_name='schools',
            name='so_schools_id_720d72_idx',
        ),
        migrations.AddIndex(
            model_name='schools',
            index=models.Index(fields=['name', 'college_name'], name='so_schools_name_782bca_idx'),
        ),
        migrations.AddField(
            model_name='department',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_domain.schools'),
        ),
        migrations.AddIndex(
            model_name='department',
            index=models.Index(fields=['name', 'school'], name='so_departme_name_5a5d6e_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='department',
            unique_together={('name', 'school')},
        ),
    ]
