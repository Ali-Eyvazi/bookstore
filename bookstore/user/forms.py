"""
user form for admin pannel
"""
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class UserCreationForm(forms.ModelForm):
    """
    from to create users in admin pannel
    """
    password1 = forms.CharField(
        label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        """
        defining details of form
        """
        model = User
        fields = ('email', 'phone_number', 'full_name',)

    def clean_password2(self):
        """
        method to check if two passwords are similar or not 
        """
        user_cleaned_data = self.cleaned_data
        if user_cleaned_data['password1'] and user_cleaned_data['password2'] and user_cleaned_data['password1'] != user_cleaned_data['password2']:
            raise ValidationError('passwords must match')
        return user_cleaned_data['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    changing user specifications
    """
    password = ReadOnlyPasswordHashField(
        help_text="you can change password using<a href=\"../password/\"> this form </a>.")

    class Meta:
        """
        defining details of form
        """
        model = User
        fields = ('email', 'phone_number', 'full_name',
                  'password', 'last_login')


class UserRegisterationForm(forms.Form):
    """
    user registration form
    """
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    full_name = forms.CharField(
        label='Full name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=11, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    def clean_email(self):
        """
        user email check for registration
        """
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email Already exists')
        return email

    def clean_password2(self):
        """
        user password check for registration
        """
        user_cleaned_data = self.cleaned_data
        if user_cleaned_data['password1'] and user_cleaned_data['password2'] and user_cleaned_data['password1'] != user_cleaned_data['password2']:
            raise ValidationError('passwords must match')

        return user_cleaned_data['password2']

    def clean_phone(self):
        """
        user phone check for registration
        """
        phone = self.cleaned_data['phone']
        user = User.objects.filter(phone_number=phone).exists()
        if user:
            raise ValidationError(
                'An other user has already has taken this phone number')

        return phone
