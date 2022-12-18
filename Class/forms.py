from django import forms
from .models import *
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'
            if fname == 'roll_id':
                f.widget.attrs['readonly'] = True
                f.widget.attrs['class']='form-control read-only'
        roll_id = Student.generate_roll_id(self)
        self.fields['roll_id'].initial = roll_id

class SignUpForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'input100'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'input100'}))
    class Meta:
        model = User
        fields = ['username','password'] #these ordering will be as follow in html form

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'
            if fname == 'roll_id':
                f.widget.attrs['readonly'] = True
                f.widget.attrs['class']='form-control read-only'
        roll_id = Query.generate_roll_id(self)
        self.fields['roll_id'].initial = roll_id