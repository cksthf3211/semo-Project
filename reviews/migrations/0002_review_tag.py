# Generated by Django 3.2.13 on 2022-11-03 15:48

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='tag',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, '별 보기 좋은'), (2, '시원한 여름'), (3, '파티가 있는'), (4, '가족이랑'), (5, '커플'), (6, '조용한'), (7, '애견동반'), (8, '도심 속 캠핑장'), (9, '풍경이 좋은'), (10, '2030인기'), (11, '바다가 보이는')], default=1, max_length=23),
            preserve_default=False,
        ),
    ]
