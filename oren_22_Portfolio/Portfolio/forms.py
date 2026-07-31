from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from Portfolio.models import*

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username','email','password1','password2']
        
class LoginForm(AuthenticationForm):
    pass

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields ='__all__'
        
        
class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields ='__all__'
        
        
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceModel
        fields ='__all__'
        
        
class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationModel
        fields ='__all__'
        widgets = {
            'passing_year': forms.DateInput(attrs={'type':'date'}),
        }