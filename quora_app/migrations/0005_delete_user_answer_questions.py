# Generated by Django 4.2 on 2025-04-10 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quora_app', '0004_alter_answer_creation_date_alter_question_content_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='answer',
            name='questions',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='quora_app.question'),
            preserve_default=False,
        ),
    ]
