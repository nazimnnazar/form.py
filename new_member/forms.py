from django import forms
from . models import NewMember
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError 

class NewMemberForm(forms.ModelForm):
    fullname = forms.CharField(
        label = 'Full Name' ,min_length=3,max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="Only Letter Is Allowed")],
        error_messages ={'requires':'The Full name is requires !'},
        widget=forms.TextInput(attrs={'placeholder':'full name'})
    )
    
    email = forms.CharField(
        label = "Email",min_length=3,max_length=30,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message="Enter Valid Email Address")],
        widget=forms.TextInput(attrs={'placeholder':'Email'})
    )
    state = forms.CharField(
        label = "State",min_length=3,max_length=14,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="Enter Currect State")],
        widget=forms.TextInput(attrs={'placeholder':'State'})
    )

    city = forms.CharField(
        label = "City",min_length=3,max_length=40,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="Enter Currect city")],
        widget=forms.TextInput(attrs={'placeholder':'City'})
    )

    GENDER = [
        ('male','male'),
        ('female','female')
    ]
    gender = forms.CharField(
        label='Gender',
        widget=forms.RadioSelect(choices=GENDER,
        attrs={'class':'form-control'})
    )
    FRESHER_EXPERIANCE = [
        ('Fresher','Fresher'),
        ('Experiance','Experiance')
    ]
    fresher_or_Experiance = forms.CharField(
        label='You are',
        widget =forms.RadioSelect(choices=FRESHER_EXPERIANCE),
    )

    SALARY = [
        ('10000-20000','10000-20000'),
        ('20000-30000','20000-30000'),
        ('30000-40000','30000-40000'),
        ('40000-50000','40000-50000'),
        ('50000-60000','50000-60000'),
        ('60000-70000','60000-70000'),
        ('70000-80000','70000-80000'),
        ('80000-90000','80000-90000'),
        ('90000-100000','90000-100000'),
        ('100000-200000','100000-200000'),
    ]
    salary = forms.CharField(
        label='Salaray expectation',
        widget=forms.Select(choices=SALARY,
        attrs={'class': 'form-control'})  
    )
    EDUCATION = [
        ('PlusTwo','PlusTwo'),
        ('BA','BA'),
        ('Bcom','Bcom'),
        ('BBA','BBA'),
        ('MA','MA'),
        ('Mcom','Mcom'),
        ('MBA','MBA'),
        ('Diploma','Diploma'),
        ('Other','Other'),
    ]
    education = forms.CharField(
        label='Education',
        widget=forms.Select(choices=EDUCATION,
        attrs={'class': 'form-control'})
    )

    JOBTYPE = [
        ('Internship','Internship'),
        ('Direct Job','Direct Job')
    ]
    jobtype = forms.CharField(
        label='Job Type',
        widget=forms.RadioSelect(choices=JOBTYPE,
        attrs = {'class':'form-control'})
    )

    resume = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'style':''
            }
        )
    )

    selfintro = forms.CharField(
        label='About you',
        min_length =10, max_length =1000,
        widget = forms.Textarea(
            attrs={
                'placeholder':'Talk a little about you'
            }
        )
    )

    class Meta:
        model = NewMember
        fields = "__all__"

        widgets={
            'birth':forms.DateInput(
                attrs={
                    'style':'font-size:16px;',
                    'type':'date',
                    'onkeydown':'retrun false',
                    'min':'1950-01-21',
                    'max':'2006-01-01',
                }
            )
        }
    # ==============Already exist Code ==============
    def clean_email(self):
        email = self.cleaned_data.get('email')
        for i in NewMember.objects.all():
            if i.email == email:
                raise forms.ValidationError('Denied !' + email + 'is already registered.')
        return email
    
    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        for i in NewMember.objects.all():
            if i.fullname == fullname:
                raise forms.ValidationError('Denied !' + fullname + 'is already registered')
        return fullname
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        for i in NewMember.objects.all():
            if i.phone == phone:
                raise forms.ValidationError('Denied' + phone + 'is already registed')
        return phone
    # ==============End Already exist==============