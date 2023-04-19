from django import forms

class StudentForm(forms.Form):
    sid=forms.IntegerField()
    name=forms.CharField(max_length=100)
    email=forms.EmailField()