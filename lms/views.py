from django.shortcuts import render, redirect
from .models import Course, Submission, Teacher, Student, CourseClassroom, StudentCourseClassroom, Notice, Assignment

from django.http import JsonResponse


def signin(request):
    if request.method == 'GET':
        return render(request, 'lms/login.html')
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pass')

        # print(type(u))
        # print(p)

        try:
            user = Teacher.objects.get(user_id=u, user_pass=p)

            request.session['user_id'] = u
            request.session['who'] = 'teacher'
            return redirect('homepage')
        except Exception as e:
            print(e)
            try:
                user = Student.objects.get(user_id=u, user_pass=p)

                request.session['user_id'] = u
                request.session['who'] = 'student'
                return redirect('homepage')
            except Exception as e:
                return redirect('login')


def home(request):
    u = request.session['user_id']
    who = request.session['who']

    context = None
    if 'teacher' in who:
        context = CourseClassroom.objects.filter(Teacher_user_id=u)
    elif 'student' in who:
        context = StudentCourseClassroom.objects.filter(Student_user_id=u)

    return render(request, 'lms/home.html', {'user_id': u, 'all': context, 'who': who})


def course_view(request, course_id):
    user_id = request.session['user_id']

    all_notice = Notice.objects.all().filter(
        course_id=course_id).order_by('-date_posted')
    all_assignment = Assignment.objects.all().filter(
        course_id=course_id).order_by('-date_posted')

    all_submission = None
    is_set_all_submission = None
    try:
        all_submission = Submission.objects.get(course_id=course_id)
        # print(all_submission.course_id.course_id.course_id.course_id)
        # print(type(all_submission))

        if 'QuerySet' in str(type(all_submission)):
            is_set_all_submission = 1
            print("hi 0")
            # print(all_assignment[0].uploaded_file)
            for i in range(len(all_assignment)):
                if 'None' in str(all_assignment[i].uploaded_file):
                    all_assignment[i].due_assignment = "yes"
                    print("hi 1")
                else:
                    all_assignment[i].due_assignment = "no"
                    print("hi 2")

        else:
            is_set_all_submission = 0
            if 'None' in str(all_assignment.uploaded_file):
                    all_assignment.due_assignment = "yes"
                    print("hi 3")
            else:
                all_assignment.due_assignment = "no"
                print("hi 4")
    except:
        is_set_all_submission = -1

    context = {'all_notice': all_notice, 'all_assignment': all_assignment,
               'all_submission': all_submission, 'is_set_all_submission':is_set_all_submission, 'course_id': course_id, 'user_id': user_id}

    try:
        print(all_assignment[0].due_assignment)
    except:
        print("not found")
        print(type(all_assignment[0].uploaded_file))
    return render(request, 'lms/courseView.html', context)


def postNotice(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        content = request.POST.get('content')

        p = Notice(course_id=CourseClassroom.objects.get(
            course_id=course_id), content=content)
        p.save()

        return redirect('courseview', course_id=course_id)

    return redirect('homepage')


def deleteNotice(request, id_notice):
    n = Notice.objects.get(id=id_notice)
    t_id = n.course_id.Teacher_user_id.user_id
    c_id = n.course_id.course_id.course_id

    if t_id == request.session['user_id']:
        n.delete()
        return redirect('courseview', id=c_id)
    else:
        return redirect('courseview', id=c_id)


def updateNotice(request, id_notice):
    if request.method == 'POST':
        n = Notice.objects.get(id=id_notice)

        course_id = request.POST.get('course_id')
        content = request.POST.get('content')

        n.content = content
        n.save()

        return redirect('courseview', course_id=course_id)

    return redirect('homepage')


def postAssignment(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')

        title = request.POST.get('title')
        content = request.POST.get('content')

        try:
            uploaded_file = request.FILES['file_path']
        except:
            uploaded_file = 'None'

        # none or on(str)
        has_submission_portal = request.POST.get('has_submission_portal')
        if has_submission_portal == None:
            has_submission_portal = '0'
        else:
            has_submission_portal = '1'

        a = Assignment(course_id=CourseClassroom.objects.get(course_id=course_id), title=title,
                       content=content, uploaded_file=uploaded_file, has_submission_portal=has_submission_portal)
        a.save()

        return redirect('courseview', course_id=course_id)
    return redirect('homepage')


def deleteAssignment(request, id_assignment):
    a = Assignment.objects.get(id=id_assignment)
    teacher_id = a.course_id.Teacher_user_id.user_id
    course_id = a.course_id.course_id.course_id

    if teacher_id == request.session['user_id']:
        a.delete()
        return redirect('courseview', course_id=course_id)
    else:
        return redirect('courseview', course_id=course_id)


def sendStudentSubmission(request, id_assignment):
    # s = list(Submission.objects.get(Assignment_id=id_assignment))
    # s = list(Notice.objects.all().filter(
    #     id=10).order_by('-date_posted').values())
    # print(s)
    # return JsonResponse(s, safe=False)
    pass


def postSubmission(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        assignment_id = request.POST.get('assignment_id')

        name = request.POST.get('name')
        try:
            uploaded_file = request.FILES['uploaded_file']
        except:
            uploaded_file = 'None'

        s = Submission(Assignment_id=Assignment.objects.get(id=assignment_id), Student_user_id=Student.objects.get(
            user_id=request.session['user_id']), course_id=StudentCourseClassroom.objects.get(course_id=course_id), name=name, uploaded_file=uploaded_file)
        s.save()

        return redirect('courseview', course_id=course_id)
    return redirect('homepage')
