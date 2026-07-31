from django.contrib import admin
from Portfolio.models import*

admin.site.register([UserModel,ProfileModel,ProjectModel,SkillModel,ExperienceModel,EducationModel])
