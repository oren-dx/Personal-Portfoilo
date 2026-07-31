from django.urls import path
from Portfolio.views import*

urlpatterns = [
    path('',register,name='register'),
    path('login/',login_page, name='login_page'),
    path('logout/',logout_page, name='logout_page'),
    
    path('dashboard/',dashboard, name='dashboard'),
    path('profile_page/',profile_page, name='profile_page'),
    path('update_profile/',update_profile, name='update_profile'),
    path('resume_page/',resume_page, name='resume_page'),
    
    path('project_list/',project_list, name='project_list'),
    path('add_project/',add_project, name='add_project'),
    path('edit_project/<str:id>/',edit_project, name='edit_project'),
    path('delete_project/<str:id>/',delete_project, name='delete_project'),
    
    path('skill_list/',skill_list, name='skill_list'),
    path('add_skill/',add_skill, name='add_skill'),
    path('edit_skill/<str:id>/',edit_skill, name='edit_skill'),
    path('delete_skill/<str:id>/',delete_skill, name='delete_skill'),
    
    path('experience_list/',experience_list, name='experience_list'),
    path('add_experience/',add_experience, name='add_experience'),
    path('edit_experience/<str:id>/',edit_experience, name='edit_experience'),
    path('delete_experience/<str:id>/',delete_experience, name='delete_experience'),
    
    path('education_list/',education_list, name='education_list'),
    path('add_education/',add_education, name='add_education'),
    path('edit_education/<str:id>/',edit_education, name='edit_education'),
    path('delete_education/<str:id>/',delete_education, name='delete_education'),
]
