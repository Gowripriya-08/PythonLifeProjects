from django.shortcuts import render
from .models import Student, Marks


# Add Student
def add_student(request):
    if request.method == "POST":
        roll = request.POST['roll']
        name = request.POST['name']
        age = request.POST['age']
        course = request.POST['course']

        Student.objects.create(
            roll=roll,
            name=name,
            age=age,
            course=course,
        )

    return render(request, 'add_students.html')


# Add Marks
def add_marks(request):
    if request.method == "POST":
        roll = request.POST['roll']
        telugu = request.POST['telugu']
        maths = request.POST['maths']
        science = request.POST['science']
        english = request.POST['english']

        student = Student.objects.get(roll=roll)

        Marks.objects.create(
            telugu=telugu,
            science=science,
            maths=maths,
            english=english,
            student=student,
        )

    return render(request, 'add_marks.html')


# View Student
def view_students(request):
    student = None
    marks = None

    if request.method == 'POST':
        roll = request.POST['roll']

        try:
            student = Student.objects.get(roll=roll)
            marks = Marks.objects.get(student=student)

        except:
            student = None
            marks = None

    return render(
        request,
        'view_students.html',
        {
            'student': student,
            'marks': marks
        }
    )
def edit_student(request):
    student = None

    if request.method == "POST":
        roll = request.POST['roll']

        student = Student.objects.get(roll=roll)

        student.name = request.POST['name']
        student.age = request.POST['age']
        student.course = request.POST['course']

        student.save()

    return render(request, 'edit_student.html', {'student': student})