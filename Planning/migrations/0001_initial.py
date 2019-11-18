# Generated by Django 2.2.4 on 2019-11-18 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=45)),
                ('exercise_type', models.CharField(choices=[('Athletic', 'Athletic'), ('Integrated', 'Integrated'), ('Reduced Play', 'Reduced Play'), ('Technique', 'Technique'), ('Tec-tac', 'Tec-tac'), ('Strategy', 'Strategy'), ('Warm-up', 'Warm-up'), ('Prevention', 'Prevention')], max_length=45)),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('duration', models.FloatField()),
                ('sequences', models.FloatField()),
                ('recovery', models.FloatField()),
                ('recovery_type', models.CharField(choices=[('Active', 'Active'), ('Passive', 'Passive')], max_length=45)),
                ('NMI', models.IntegerField()),
                ('effort_perception', models.IntegerField()),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_label', models.CharField(max_length=255)),
                ('question_text', models.TextField()),
                ('question_scale', models.PositiveIntegerField()),
                ('question_positive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('logo', models.ImageField(default='default_pic.png', upload_to='logo_pics')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_label', models.CharField(max_length=255)),
                ('survey_timing', models.CharField(choices=[('Anterior', 'Anterior'), ('Posterior', 'Posterior')], max_length=20)),
                ('survey_questions', models.ManyToManyField(to='Planning.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_date', models.DateTimeField()),
                ('exercises', models.ManyToManyField(to='Planning.Exercise')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Planning.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('shoe_size', models.FloatField()),
                ('vetemenent_size', models.FloatField()),
                ('number', models.IntegerField()),
                ('post', models.IntegerField()),
                ('foot_of_strong', models.CharField(max_length=5)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='player_creator', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='Planning.Team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_answer', models.FloatField()),
                ('answer_valid', models.BooleanField(default=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Planning.Player')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Planning.Question')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Planning.Session')),
            ],
            options={
                'unique_together': {('player', 'session', 'question')},
            },
        ),
    ]
