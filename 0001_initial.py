import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(name='Course', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('name', models.CharField(default='Online Course', max_length=100)), ('description', models.CharField(default='Course description', max_length=500)), ('pub_date', models.DateField(default=django.utils.timezone.now)), ('total_enrollment', models.IntegerField(default=0))]),
        migrations.CreateModel(name='Instructor', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('full_time', models.BooleanField(default=True)), ('total_learners', models.IntegerField(default=0)), ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL))]),
        migrations.CreateModel(name='Learner', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('occupation', models.CharField(choices=[('student', 'Student'), ('developer', 'Developer'), ('data_scientist', 'Data Scientist'), ('dba', 'Database Admin')], default='student', max_length=20)), ('social_link', models.URLField(default='')), ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL))]),
        migrations.CreateModel(name='Lesson', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('title', models.CharField(default='Lesson', max_length=200)), ('content', models.TextField(default='Lesson content')), ('order', models.IntegerField(default=0)), ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course'))]),
        migrations.CreateModel(name='Enrollment', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('date_enrolled', models.DateTimeField(default=django.utils.timezone.now)), ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course')), ('learner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.learner'))]),
        migrations.CreateModel(name='Question', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('question_text', models.CharField(max_length=500)), ('grade', models.IntegerField(default=1)), ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course'))]),
        migrations.CreateModel(name='Choice', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('choice_text', models.CharField(max_length=500)), ('is_correct', models.BooleanField(default=False)), ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'))]),
        migrations.CreateModel(name='Submission', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('choices', models.ManyToManyField(to='onlinecourse.choice')), ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.enrollment'))]),
        migrations.AlterUniqueTogether(name='enrollment', unique_together={('learner', 'course')}),
    ]
