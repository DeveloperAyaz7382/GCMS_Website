# forms.py
from django import forms
from .models import VisitRequest

class VisitRequestForm(forms.ModelForm):
    class Meta:
        model = VisitRequest
        fields = ['name', 'email', 'phone', 'interest', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
            'interest': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('Computer Labs', 'Computer Labs'),
                ('Hostel Facilities', 'Hostel Facilities'),
                ('Both', 'Both'),
                ('Other Facilities', 'Other Facilities'),
            ]),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Your Message'}),

        }



from .models import OnlineApplication

class OnlineApplicationForm(forms.ModelForm):
    class Meta:
        model = OnlineApplication
        fields = [
            'full_name',
            'email',
            'phone',
            'address',
            'program',
            'previous_institute',
            'year_completed',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Enter your full address'}),
            'program': forms.Select(attrs={'class': 'form-select'}),
            'previous_institute': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Previous school/college'}),
            'year_completed': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 2024'}),
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'address': 'Address',
            'program': 'Program of Interest',
            'previous_institute': 'Previous Institute',
            'year_completed': 'Year of Completion',
        }