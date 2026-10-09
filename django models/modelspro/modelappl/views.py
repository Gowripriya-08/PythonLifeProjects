from django.shortcuts import render, redirect, get_object_or_404
from .models import students


def student_form(request):
    message = ""

    if request.method == "POST":
        students.objects.create(
            name=request.POST["name"],
            rollnumber=request.POST["roll_number"],
            student_class=request.POST["class"],
            age=request.POST["age"],
            parent_contact=request.POST["parent_contact"]
        )

        message = "Student added successfully"

    return render(request, "student.html", {"message": message})


def student_list(request):
    all_students = students.objects.all()

    return render(
        request,
        "student_list.html",
        {"students": all_students}
    )


def student_update(request, id):
    student = get_object_or_404(students, id=id)

    if request.method == "POST":
        student.name = request.POST["name"]
        student.rollnumber = request.POST["roll_number"]
        student.student_class = request.POST["class"]
        student.age = request.POST["age"]
        student.parent_contact = request.POST["parent_contact"]

        student.save()

        return redirect("student_list")

    return render(request, "student_update.html", {"student": student})


def student_delete(request, id):
    student = get_object_or_404(students, id=id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "student_delete.html", {"student": student})