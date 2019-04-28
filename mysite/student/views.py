from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserLoginForm, UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.apps import apps
Profile=apps.get_model('project','Profile')
CT_Marks=apps.get_model('project','CT_Marks')
from django.contrib.auth.decorators import login_required

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

def home(request):
    return render(request, 'student/home.html', {})

def register_view(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('/login/')
    else:
        form = UserRegisterForm()
    return render(request, 'project/register.html', {'form': form})

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/home/')

    context = {
        'form': form,
    }
    return render(request, "project/login.html", context)
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):

    return render(request,'student/profile.html')

@login_required
def update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'student/update.html',context)

def ct_marks(request):
    items = CT_Marks.objects.all()
    context ={
        'items' : items,
        'header' : "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)

def about(request):
    return render(request, 'student/about.html', {'title': 'about'})

def contact(request):
    return render(request, 'student/contact.html', {'title': 'contact'})

def CHEM_1113(request):
    items = CT_Marks.objects.filter(course_name='Chemistry')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_1101(request):
    items = CT_Marks.objects.filter(course_name='Computer Programming')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def EEE_1151(request):
    items = CT_Marks.objects.filter(course_name='Basic Electrical Engineering')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def MATH_1113(request):
    items = CT_Marks.objects.filter(course_name='Differential and Integral Calculus')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def HUM_1113(request):
    items = CT_Marks.objects.filter(course_name='Functional English')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
def CSE_1201(request):
    items = CT_Marks.objects.filter(course_name='Data Structure')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_1203(request):
    items = CT_Marks.objects.filter(course_name='Object Oriented Programming')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)

    return render(request, 'student/ct_marks.html', context)
def MATH_1213(request):
    items = CT_Marks.objects.filter(course_name='Co-ordinate Geometry')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def HUM_1213(request):
    items = CT_Marks.objects.filter(course_name='Economics and Sociology')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def PHY_1213(request):
    items = CT_Marks.objects.filter(course_name='Physics')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_2101(request):
    items = CT_Marks.objects.filter(course_name='Discrete Mathematics')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_2103(request):
    items = CT_Marks.objects.filter(course_name='Numerical Methods')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def EEE_2151(request):
    items = CT_Marks.objects.filter(course_name='Analog Electronics')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def MATH_2113(request):
    items = CT_Marks.objects.filter(course_name='Vector Analysis and Algebra')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def HUM_2113(request):
    items = CT_Marks.objects.filter(course_name='Management and Accounting')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_2201(request):
    items = CT_Marks.objects.filter(course_name='Computer Algorithms')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_2203(request):
    items = CT_Marks.objects.filter(course_name='Digital Techniques')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_2205(request):
    items = CT_Marks.objects.filter(course_name='Finite Automata Theory')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def EEE_2251(request):
    items = CT_Marks.objects.filter(course_name='Electrical Machines')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def MATH_2213(request):
    items = CT_Marks.objects.filter(course_name='Complex variable')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_3101(request):
    items = CT_Marks.objects.filter(course_name='Database Systems')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_3103(request):
    items = CT_Marks.objects.filter(course_name='Data Communication')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_3105(request):
    items = CT_Marks.objects.filter(course_name='Software Engineering')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_3107(request):
    items = CT_Marks.objects.filter(course_name='Applied Statistics')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_3109(request):
    items = CT_Marks.objects.filter(course_name='Assembly Language')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_3201(request):
    items = CT_Marks.objects.filter(course_name='Operating Systems')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_3203(request):
    items = CT_Marks.objects.filter(course_name='Computer Architecture and Design')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_3205(request):
    items = CT_Marks.objects.filter(course_name='Computer Networks')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_3207(request):
    items = CT_Marks.objects.filter(course_name='Peripherals and Interfacings')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_3209(request):
    items = CT_Marks.objects.filter(course_name='Artificial Intelligence')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_4101(request):
    items = CT_Marks.objects.filter(course_name='Compiler Design')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_4103(request):
    items = CT_Marks.objects.filter(course_name='Digital Signal Processing')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_4105(request):
    items = CT_Marks.objects.filter(course_name='Digital Image Processing')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_4107(request):
    items = CT_Marks.objects.filter(course_name='Information System Analysis')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_4109(request):
    items = CT_Marks.objects.filter(course_name='Unix Programming')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_4201(request):
    items = CT_Marks.objects.filter(course_name='Computer Graphics')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_4203(request):
    items = CT_Marks.objects.filter(course_name='Neural Networks')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_4205(request):
    items = CT_Marks.objects.filter(course_name='CSE_4205')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_4207(request):
    items = CT_Marks.objects.filter(course_name='CSE 4207')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)
def CSE_4209(request):
    items = CT_Marks.objects.filter(course_name='CSE 4209')
    context = {
        'items': items,
        'header': "CT_MARKs"
    }
    return render(request, 'student/ct_marks.html', context)