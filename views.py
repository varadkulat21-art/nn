from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Course, Enrollment, Learner, Submission


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lesson_set.order_by('order')
    questions = course.question_set.all()
    enrolled = False
    if request.user.is_authenticated:
        learner = Learner.objects.filter(user=request.user).first()
        enrolled = bool(learner and Enrollment.objects.filter(learner=learner, course=course).exists())
    return render(request, 'onlinecourse/course_details_bootstrap.html', {
        'course': course, 'lessons': lessons, 'questions': questions, 'enrolled': enrolled,
    })


@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    learner, _ = Learner.objects.get_or_create(user=request.user)
    enrollment, created = Enrollment.objects.get_or_create(learner=learner, course=course)
    if created:
        course.total_enrollment += 1
        course.save(update_fields=['total_enrollment'])
    return HttpResponseRedirect(reverse('onlinecourse:course_details', args=(course.id,)))


@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    learner = get_object_or_404(Learner, user=request.user)
    enrollment = get_object_or_404(Enrollment, learner=learner, course=course)
    submission = Submission.objects.create(enrollment=enrollment)
    for question in course.question_set.all():
        for choice_id in request.POST.getlist(f'choice_{question.id}'):
            choice = get_object_or_404(Choice, pk=int(choice_id), question=question)
            submission.choices.add(choice)
    return HttpResponseRedirect(reverse('onlinecourse:show_exam_result', args=(course.id, submission.id)))


@login_required
def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id, enrollment__course=course)
    selected_ids = set(submission.choices.values_list('id', flat=True))
    total_score = 0
    possible = 0
    results = []
    for question in course.question_set.all():
        possible += question.grade
        selected_for_question = [str(choice_id) for choice_id in selected_ids
            if submission.choices.filter(pk=choice_id, question=question).exists()]
        correct = question.is_get_score(selected_for_question)
        if correct:
            total_score += question.grade
        results.append({
            'question': question,
            'choices': question.choice_set.all(),
            'selected_ids': {int(value) for value in selected_for_question},
            'correct': correct,
        })
    grade = round(100 * total_score / possible) if possible else 0
    context = {
        'course': course,
        'submission': submission,
        'results': results,
        'grade': grade,
        'total_score': total_score,
        'possible': possible,
        'max_score': possible,
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
