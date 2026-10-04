from django.db import models
from django import forms
# Create your models here.

class StudentForm(forms.Form):
# needed Field - Widget 
# Student Name [Text Box] 
# Student ID [Text Box] 
# Major [Drop-down List]
# Class Standing [Radio Buttons]
# Programming Languages Known [Checkboxes]
# Expected Graduation Year [Number Input]
# Comments [Multi-line Text Area]
# Submit [Button]
    student_majors = (
        ('CS', 'Computer Science'),
        ('DS', 'Data Science'),
        ('IT', 'Information Technology'),
        ('BI', 'Bioinformatics'),
        ('En', 'Engineering')
    )

    class_std = (
        ('Fr', 'Freshman'),
        ('So','Sophmore'),
        ('Jr','Junior'),
        ('Sr','Senior'),
    )


    stud_name = forms.CharField(max_length=50, widget=forms.TextInput)
    stud_id = forms.CharField(max_length=20, widget=forms.TextInput)
    major = forms.ChoiceField(choices=student_majors, widget=forms.Select)
    class_standing = forms.ChoiceField(choices=class_std, widget=forms.RadioSelect)
    prog_languages = forms.MultipleChoiceField(
        choices=[('Python', 'Python'),
            ('Java', 'Java'),
            ('JavaScript', 'JavaScript'),
            ('C++', 'C++'),
            ('Ruby', 'Ruby')
        ],
        widget=forms.CheckboxSelectMultiple
    )
    grad_year = forms.IntegerField(widget=forms.NumberInput)
    comments = forms.CharField(widget=forms.Textarea)
