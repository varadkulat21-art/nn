from django.contrib import admin
from .models import Choice, Course, Instructor, Learner, Lesson, Question, Submission

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 3

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date', 'total_enrollment')
    list_filter = ['pub_date']
    search_fields = ('name',)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'grade', 'course')
    search_fields = ('question_text',)

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('enrollment',)
    readonly_fields = ('enrollment',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)
