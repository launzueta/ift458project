from django import forms
from django.contrib.auth.forms import UserCreationForm
from backend.models import SPVUser


class UserRegistrationForm(UserCreationForm):
    prefix_choices = (
        ("1", ""),
        ("2", "Dr."),
        ("3", "Mr."),
        ("4", "Mrs."),
        ("5", "Mrs."),
    )
    prefix = forms.ChoiceField(label="Appellation", choices=prefix_choices)

    class Meta:
        model = SPVUser
        fields = [
            'username',
            'firstname',
            'middlename',
            'lastname',
            'jobtitle',
            'email',
            'officephone',
            'cellphone',
            'prefix',
            'clientID',
            'is_staff'
        ]
        labels = {
            'firstname': 'First Name',
            'middlename': 'Middle Name',
            'lastname': 'Last Name',
            'jobtitle': 'Job Title',
            'officephone': 'Office Phone',
            'cellphone': 'Cell Phone',
            'prefix': 'Appellation',
            'clientID': 'Company',
            'is_staff': 'Staff'
        }
