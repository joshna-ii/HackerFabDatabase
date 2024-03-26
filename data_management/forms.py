from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from data_management.models import AluminumEtch, AluminumEvaporation, ChipList, ChipListSearch, Deposition, OxideEtch, Patterning, PlasmaClean, PlasmaEtch

class AluminumEtchSearchForm(forms.ModelForm):
    class Meta:
        model = AluminumEtch
        exclude = (
            'AluminumEtch_metrology_link',
            'chip_owner',
            'chip_number',
            'picture',
            'content_type',
        )
        labels = {
            'chip_owner': "Enter Username",
        }

class AluminumEvaporationSearchForm(forms.ModelForm):
    class Meta:
        model = AluminumEvaporation
        exclude = (
            'AluminumEvaporation_metrology_link',
            'chip_owner',
            'chip_number',
            'picture',
            'content_type',
        )
        labels = {
            'chip_owner': "Enter Username",
        }

class ChipListSearchForm(forms.ModelForm):
    class Meta:
        model = ChipListSearch
        exclude = ()
        labels = {
        }

class DepositionSearchForm(forms.ModelForm):
    class Meta:
        model = Deposition
        exclude = (
            'Deposition_metrology_link',
            'chip_owner',
            'chip_number',
            'picture',
            'content_type',
        )
        labels = {
            'chip_owner': "Enter Username",
        }

class OxideEtchSearchForm(forms.ModelForm):
    class Meta:
        model = OxideEtch
        exclude = (
            'OxideEtch_metrology_link',
            'chip_owner',
            'chip_number',
            'picture',
            'content_type',
        )
        labels = {
            'chip_owner': "Enter Username",
        }

class PatterningSearchForm(forms.ModelForm):
    class Meta:
        model = Patterning
        exclude = (
            'Patterning_metrology_link',
            'chip_owner',
            'chip_number',
            'picture',
            'content_type',
        )
        labels = {
            'chip_owner': "Enter Username",
        }

class PlasmaCleanSearchForm(forms.ModelForm):
    class Meta:
        model = PlasmaClean
        exclude = (
            'PlasmaClean_metrology_link',
            'chip_owner',
            'chip_number',
            'picture',
            'content_type',
        )
        labels = {
            'chip_owner': "Enter Username",
        }

class PlasmaEtchSearchForm(forms.ModelForm):
    class Meta:
        model = PlasmaEtch
        exclude = (
            'PlasmaEtch_metrology_link',
            'chip_owner',
            'chip_number',
            'picture',
            'content_type',
        )
        labels = {
            'chip_owner': "Enter Username",
        }

class AluminumEtchInputForm(forms.ModelForm):
    class Meta:
        model = AluminumEtch
        exclude = (
            'chip_owner',
            'AluminumEtch_step_time',
            'content_type',
        )

class AluminumEvaporationInputForm(forms.ModelForm):
    class Meta:
        model = AluminumEvaporation
        exclude = (
            'chip_owner',
            'AluminumEvaporation_step_time',
            'content_type',
        )

class ChipListForm(forms.ModelForm):
    class Meta:
        model = ChipList
        exclude = (
            'chip_owner',
            'chip_number',
            'creation_time',
        )

class DepositionInputForm(forms.ModelForm):
    class Meta:
        model = Deposition
        exclude = (
            'chip_owner',
            'Deposition_step_time',
            'content_type',
        )

class OxideEtchInputForm(forms.ModelForm):
    class Meta:
        model = OxideEtch
        exclude = (
            'chip_owner',
            'OxideEtch_step_time',
            'content_type',
        )

class PatterningInputForm(forms.ModelForm):
    class Meta:
        model = Patterning
        exclude = (
            'chip_owner',
            'Patterning_step_time',
            'content_type',
        )

class PlasmaCleanInputForm(forms.ModelForm):
    class Meta:
        model = PlasmaClean
        exclude = (
            'chip_owner',
            'PlasmaClean_step_time',
            'content_type',
        )

class PlasmaEtchInputForm(forms.ModelForm):
    class Meta:
        model = PlasmaEtch
        exclude = (
            'chip_owner',
            'PlasmaEtch_step_time',
            'content_type',
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