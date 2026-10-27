# Assignment 06 – Django Online Course App (15 pts)

Full exam assessment flow verified live: admin sections, course page,
exam submit → Congratulations + Score 100/100 (100%).

## Code (in this folder, mirrored to GitHub repo root)

- `onlinecourse/models.py` – Course, Lesson, **Instructor**, **Learner**, **Question**, **Choice**, **Submission**
- `onlinecourse/admin.py` – 7 imports (admin + Course, Lesson, Instructor, Learner,
  Question, Choice, Submission), QuestionInline, ChoiceInline, QuestionAdmin,
  LessonAdmin (+ CourseAdmin with `list_filter`, SubmissionAdmin)
- `onlinecourse/templates/onlinecourse/course_details_bootstrap.html` – course name,
  lessons loop, Bootstrap exam form
- `onlinecourse/views.py` – `submit`, `show_exam_result` (+ course_details, enroll)
- `onlinecourse/urls.py` – `submit` and `show_exam_result` paths

## GitHub submission (repo MUST be named `tfjzl-final-cloud-app-with-database`)

E.g. `https://github.com/Vedant-Divate/tfjzl-final-cloud-app-with-database/blob/main/onlinecourse/models.py`
(same pattern for admin.py, course_details_bootstrap.html, views.py, urls.py).

## Screenshots (in this folder)

- `03-admin-site.png` – Authentication and Authorization + OnlineCourse sections
- `07-final.png` – Congratulations, Score 100/100 (100%), per-question results

## Run

```bash
pip install django
python manage.py migrate
python manage.py runserver   # admin admin/admin123, student student/student123
```

Committed locally on branch `assignment-06-django-course`; `main` untouched.
