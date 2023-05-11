from django import forms
from .models import Reservation, DateOptions

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'nameStudent', 'school', 'grade', 'desired_class',
            'parents_phone_number', 'time', 'date'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'id': 'date_input'}), # Replace 'date_field' with the actual name of the date field in your model
        }
        
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True