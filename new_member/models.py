from django.db import models
from multiselectfield import MultiSelectField

FRAMEWORKS = (
    ('Django','Django'),
    ('Flask','Flask'),
    ('Vue','Vue'),
    ('Angular','Angular'),
    ('ASP.NET Core','ASP.NET Core'),
)
LANGUAGES =(
    ('Python','Python'),
    ('Java','Java'),
    ('C++','C++'),
    ('Javascript','Javascript'),
    ('PHP','PHP'),
)
DATABASE = (
    ('MySQL','MySQL'),
    ('Postgree','Postgree'),
    ('MongoDB','MongoDB'),
    ('FireBase','Firebase'),
    ('Oracle','Oracle'),
)
LIBRARIES = (
    ('Ajax','Ajax'),
    ('Jquery','Jquery'),
    ('React.js','React.js'),
    ('Chart.js','Chart.js'),
    ('Gsap','Gsap'),
)
OTHER = (
    ('Git','Git'),
    ('Bootstrap','Bootstrap'),
    ('Docker','Docker'),
    ('SQL','SQL'),
    ('GraphQL','GraphQL'),
)

class NewMember(models.Model):
    fullname = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    birth = models.DateField(auto_now=False,auto_now_add=False,verbose_name="Birthday")
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    gender = models.CharField(max_length=250)
    education = models.CharField(max_length=250)
    jobtype = models.CharField(max_length=250)
    resume = models.FileField()
    frameworks = MultiSelectField(choices=FRAMEWORKS,default="",max_length=200)
    languages = MultiSelectField(choices=LANGUAGES,default="",max_length=200)
    database = MultiSelectField(choices=DATABASE,default="",max_length=200)
    libraries = MultiSelectField(choices=LIBRARIES,default="",max_length=200)
    other = MultiSelectField(choices=OTHER,default="",max_length=200)
    fresher_or_Experiance = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    selfintro = models.TextField()

