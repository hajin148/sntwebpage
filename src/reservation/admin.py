from django.contrib import admin
from reservation.models import Reservation, DateOptions

class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'nameStudent',
        'date',
        'parents_phone_number',
        'school',
        'grade',
        'desired_class',
        'time',
    )

class DateOptionsAdmin(admin.ModelAdmin):
    list_display = ('date', 'capacity',)  # Add capacity field here


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(DateOptions, DateOptionsAdmin)
