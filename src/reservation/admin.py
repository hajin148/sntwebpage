from django.contrib import admin
from reservation.models import Reservation, DateOptions, TimeOption

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

class TimeOptionInline(admin.TabularInline):
    model = DateOptions.time_options.through
    extra = 1

class DateOptionsAdmin(admin.ModelAdmin):
    inlines = [TimeOptionInline]
    list_display = ('date',)
    exclude = ('time_options',)

class TimeOptionAdmin(admin.ModelAdmin):
    list_display = ('time', 'capacity')

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(DateOptions, DateOptionsAdmin)
admin.site.register(TimeOption, TimeOptionAdmin)
