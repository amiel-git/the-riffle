from django import forms
from accounts.models import Profile

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'email',
            'first_name',
            'last_name',
            'address',
            'contact_number',
            'password'
        ]
        widgets = {
            'email': forms.widgets.EmailInput(attrs={'class':'form-control'}),
            'first_name': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'address': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'contact_number': forms.widgets.NumberInput(attrs={'class':'form-control'}),
            'password': forms.widgets.PasswordInput(attrs={'class':'form-control'}),
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user