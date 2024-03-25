from django import forms
from school.models import Teacher, Activity, Schedule, Zanyatie, Enrollment

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['date', 'time', 'comments']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }