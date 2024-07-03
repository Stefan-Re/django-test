from student.models import Student


def get_all_students(request):
    return {'students': Student.objects.all()}