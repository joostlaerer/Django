from django import forms
from .models import Volunteer


class VolunteerSignupForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['first_name', 'last_name', 'email', 'phone', 'skills', 'availability', 'bio']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number (optional)'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'e.g., Teaching, Web Development, or just one skill', 'rows': 3}),
            'availability': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Weekends, Evenings, Flexible'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us about yourself', 'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make optional fields explicitly not required
        self.fields['phone'].required = False
        self.fields['skills'].required = False
        self.fields['availability'].required = False
        self.fields['bio'].required = False
