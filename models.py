from django.conf import settings
from django.db import models
from django.utils.timezone import now


class Course(models.Model):
    name = models.CharField(max_length=100, default='Online Course')
    description = models.CharField(max_length=500, default='Course description')
    pub_date = models.DateField(default=now)
    total_enrollment = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='Lesson')
    content = models.TextField(default='Lesson content')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Instructor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Learner(models.Model):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'), (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'), (DATABASE_ADMIN, 'Database Admin'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=20, choices=OCCUPATION_CHOICES, default=STUDENT)
    social_link = models.URLField(max_length=200, default='')

    def __str__(self):
        return self.user.username


class Enrollment(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(default=now)

    class Meta:
        unique_together = ('learner', 'course')

    def __str__(self):
        return f'{self.learner} - {self.course}'


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text

    def is_get_score(self, selected_ids):
        correct_ids = set(self.choice_set.filter(is_correct=True).values_list('id', flat=True))
        return correct_ids == set(int(i) for i in selected_ids)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return f'Submission: {self.enrollment}'
