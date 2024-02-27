from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from data_management.models import AluminumEtch, AluminumEvaporation, ChipList, DepositionTemplate, OxideEtch, Patterning, PlasmaClean, PlasmaEtch

class AluminumEtchSearchForm(forms.ModelForm):
    class Meta:
        model = AluminumEtch
        exclude = (
            'metrology_link',
            'chip_owner',
            'chip_number',
        )
        labels = {
            'chip_owner': "Enter Username",
        }

class AluminumEvaporationSearchForm(forms.ModelForm):
    class Meta:
        model = AluminumEvaporation
        exclude = (
            'metrology_link',
            'chip_owner',
            'chip_number',
        )
        labels = {
            'chip_owner': "Enter Username",
        }

class ChipListSearchForm(forms.ModelForm):
    class Meta:
        model = ChipList
        exclude = ()
        labels = {
        }

class DepositionTemplateSearchForm(forms.ModelForm):
    class Meta:
        model = DepositionTemplate
        exclude = (
            'metrology_link',
            'chip_owner',
            'chip_number',
        )
        labels = {
            'chip_owner': "Enter Username",
        }

class OxideEtchSearchForm(forms.ModelForm):
    class Meta:
        model = OxideEtch
        exclude = (
            'metrology_link',
            'chip_owner',
            'chip_number',
        )
        labels = {
            'chip_owner': "Enter Username",
        }

class PatterningSearchForm(forms.ModelForm):
    class Meta:
        model = Patterning
        exclude = (
            'metrology_link',
            'chip_owner',
            'chip_number',
        )
        labels = {
            'chip_owner': "Enter Username",
        }

class PlasmaCleanSearchForm(forms.ModelForm):
    class Meta:
        model = PlasmaClean
        exclude = (
            'metrology_link',
            'chip_owner',
            'chip_number',
        )
        labels = {
            'chip_owner': "Enter Username",
        }

class PlasmaEtchSearchForm(forms.ModelForm):
    class Meta:
        model = PlasmaEtch
        exclude = (
            'metrology_link',
            'chip_owner',
            'chip_number',
        )
        labels = {
            'chip_owner': "Enter Username",
        }

class AluminumEtchForm(forms.ModelForm):
    class Meta:
        model = AluminumEtch
        exclude = (
            'chip_owner',
            'creation_time',
        )

class AluminumEvaporationForm(forms.ModelForm):
    class Meta:
        model = AluminumEvaporation
        exclude = (
            'chip_owner',
            'creation_time',
        )

class ChipListForm(forms.ModelForm):
    class Meta:
        model = ChipList
        exclude = ()

class DepositionTemplateForm(forms.ModelForm):
    class Meta:
        model = DepositionTemplate
        exclude = (
            'chip_owner',
            'creation_time',
        )

class OxideEtchForm(forms.ModelForm):
    class Meta:
        model = OxideEtch
        exclude = (
            'chip_owner',
            'creation_time',
        )

class PatterningForm(forms.ModelForm):
    class Meta:
        model = Patterning
        exclude = (
            'chip_owner',
            'creation_time',
        )

class PlasmaCleanForm(forms.ModelForm):
    class Meta:
        model = PlasmaClean
        exclude = (
            'chip_owner',
            'creation_time',
        )

class PlasmaEtchForm(forms.ModelForm):
    class Meta:
        model = PlasmaEtch
        exclude = (
            'chip_owner',
            'creation_time',
        )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super().clean()

        # Confirms that the two password fields match
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Invalid username/password")

        # We must return the cleaned data we got from our parent.
        return cleaned_data
    
class RegisterForm(forms.Form):
    username   = forms.CharField(max_length=20)
    password  = forms.CharField(max_length=200,
                                 label='Password', 
                                 widget=forms.PasswordInput())
    confirm_password  = forms.CharField(max_length=200,
                                 label='Confirm',  
                                 widget=forms.PasswordInput())
    email      = forms.CharField(max_length=50,
                                 widget = forms.EmailInput())
    first_name = forms.CharField(max_length=20)
    last_name  = forms.CharField(max_length=20)

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super().clean()

        # Confirms that the two password fields match
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('confirm_password')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")

        # We must return the cleaned data we got from our parent.
        return cleaned_data

    # Customizes form validation for the username field.
    def clean_username(self):
        # Confirms that the username is not already present in the
        # User model database.
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")

        # We must return the cleaned data we got from the cleaned_data
        # dictionary
        return username