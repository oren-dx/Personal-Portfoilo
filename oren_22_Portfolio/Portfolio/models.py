from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    
    def __str__(self):
        return f'{self.username}'
    
class ProfileModel(models.Model):
    full_name = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='profile_image/',null=True)
    address = models.TextField(null=True)
    social_link = models.URLField(null=True)
    
    def __str__(self):
            return f'{self.full_name}'
    
    
class ProjectModel(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='project/',null=True)

    def __str__(self):
        return f'{self.title}'
    
class SkillModel(models.Model):
    name = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f'{self.name}'
    
class ExperienceModel(models.Model):
    designation = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    company = models.CharField(max_length=150,null=True)
    duration = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.designation}'


class EducationModel(models.Model):
    name = models.CharField(max_length=100,null=True)
    institute = models.CharField(max_length=120,null=True)
    grade = models.CharField(null=True)
    passing_year = models.DateField(null=True)
    

    def __str__(self):
        return f'{self.name}'

