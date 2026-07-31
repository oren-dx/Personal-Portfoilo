from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from Portfolio.models import*
from .forms import  *
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'User created successfully')
            return redirect('login_page')
    else:
        messages.warning(request, 'User already exists')
        user_form = RegisterForm()

    context = {
        'user_form': user_form
    }
    return render(request, 'auth/register.html', context)

def login_page(request):
    if request.method == 'POST':
        user_form = LoginForm(request, request.POST)
        if user_form.is_valid():
            user = user_form.get_user()
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('dashboard')
    messages.success(request, 'Invaild credentials')    
    user_form = LoginForm()
    
    context = {
        'user_form':user_form
    }   
    return render(request, 'auth/login_page.html',context)

def logout_page(request):
    logout(request)
    return redirect('login_page')

def dashboard(request):
    
    return render(request, 'dashboard.html')

def profile_page(request):
    profile_data = ProjectModel.objects.first()
    
    context = {
        'profile_data':profile_data
    }
    return render(request, 'profile.html',context)

def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form_data = UpdateProfileForm(request.POST, request.FILES, instance=user)
        if form_data.is_valid():
            form_data.save()
            return redirect('profile_page')
    
    form_data = UpdateProfileForm(instance=user)
    
    context = {
        'form_data':form_data,
        'title': "Update Profile Info",
        'btn_name':"Update",
    }
    return render(request, 'base-form.html',context)

def resume_page(request):
    project_data = ProjectModel.objects.all()
    skill_data = SkillModel.objects.all()
    experience_data = ExperienceModel.objects.all()
        
    context = {
        'project_data':project_data,
        'skill_data':skill_data,
        'experience_data':experience_data,
    }
    
    return render(request, 'resume.html',context)

def project_list(request):
    project_data = ProjectModel.objects.all()
    
    context ={
        'project_data':project_data        
    }
    return render(request, 'project_list.html',context)

def add_project(request):
    if request.method == 'POST':
        form_data = ProjectForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('project_list')
    form_data = ProjectForm()
    
    context = {
        'form_data':form_data,
        'title': "Add project Info",
        'btn_name':"Add Project",
    }
    return render(request, 'base-form.html',context)


def edit_project(request, id):
    data = ProjectModel.objects.get(id = id)
    if request.method == 'POST':
        form_data = ProjectForm(request.POST, request.FILES, instance=data)
        if form_data.is_valid():
            form_data.save()
            return redirect('project_list')
    form_data = ProjectForm(instance=data)
    
    context = {
        'form_data':form_data,
        'title': "Update project Info",
        'btn_name':"Update Project",
    }
    return render(request, 'base-form.html',context)

def delete_project(request, id):
    ProjectModel.objects.get(id = id).delete()
    return redirect('project_list')

def skill_list(request):
    skill_data = SkillModel.objects.all()
    
    context = {
        'skill_data':skill_data
    }
    return render(request, 'skill_list.html',context)

def add_skill(request):
    if request.method == 'POST':
        form_data = SkillForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('skill_list')
    else:
        form_data = SkillForm()

    context = {
        'form_data': form_data,
        'title':'Add Skill Info',
        'btn_name':'Add Skill',
    }
    return render(request, 'base-form.html', context)

def edit_skill(request, id):
    data = SkillModel.objects.get(id = id)
    if request.method == 'POST':
        form_data = SkillForm(request.POST, instance=data)
        if form_data.is_valid():
            form_data.save()
            return redirect('skill_list')
    form_data = SkillForm(instance=data)
    
    context = {
        'form_data':form_data,
        'title': "Update skill Info",
        'btn_name':"Update skill",
    }
    return render(request, 'base-form.html',context)

def delete_skill(request, id):
    SkillModel.objects.get(id = id).delete()
    return redirect('skill_list')

def experience_list(request):
    experience_data = ExperienceModel.objects.all()
    
    context = {
        'experience_data':experience_data
    }
    return render(request, 'experience_list.html',context)

def add_experience(request):
    if request.method == 'POST':
        form_data = ExperienceForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('experience_list')
    else:
        form_data = ExperienceForm()

    context = {
        'form_data': form_data,
        'title':'Add Experience Info',
        'btn_name':'Add Experience',
    }
    return render(request, 'base-form.html', context)

def edit_experience(request, id):
    data = ExperienceModel.objects.get(id = id)
    if request.method == 'POST':
        form_data = ExperienceForm(request.POST, instance=data)
        if form_data.is_valid():
            form_data.save()
            return redirect('experience_list')
    form_data = ExperienceForm(instance=data)
    
    context = {
        'form_data':form_data,
        'title': "Update Experirnce Info",
        'btn_name':"Update Experirnce",
    }
    return render(request, 'base-form.html',context)

def delete_experience(request, id):
    ExperienceModel.objects.get(id = id).delete()
    return redirect('experience_list')

def education_list(request):
    education_data = EducationModel.objects.all()
    
    context = {
        'education_data':education_data
    }
    return render(request, 'education_list.html',context)

def add_education(request):
    if request.method == 'POST':
        form_data = EducationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('education_list')
    else:
        form_data = EducationForm()

    context = {
        'form_data': form_data,
        'title':'Add education Info',
        'btn_name':'Add education',
    }
    return render(request, 'base-form.html', context)

def edit_education(request, id):
    data = EducationModel.objects.get(id = id)
    if request.method == 'POST':
        form_data = EducationForm(request.POST, instance=data)
        if form_data.is_valid():
            form_data.save()
            return redirect('education_list')
    form_data = EducationForm(instance=data)
    
    context = {
        'form_data':form_data,
        'title': "Update education Info",
        'btn_name':"Update education",
    }
    return render(request, 'base-form.html',context)

def delete_education(request, id):
    EducationModel.objects.get(id = id).delete()
    return redirect('education_list')



