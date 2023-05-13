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

    def save(self, commit=True):
        reservation = super(ReservationForm, self).save(commit=False)
        if commit:
            # Decrement the capacity of the associated date
            date_option = DateOptions.objects.get(date=reservation.date)
            if date_option.capacity > 0:
                date_option.capacity -= 1
                date_option.save()
                reservation.save()
            else:
                raise forms.ValidationError("예약이 완료된 날짜입니다.")
        return reservation
