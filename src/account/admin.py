from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


def reset_password_to_default(modeladmin, request, queryset):	
	default_password = "SNT123456789!"  # Replace this with your desired default password
	for user in queryset:
		user.set_password(default_password)
		user.save()
reset_password_to_default.short_description = "비밀번호 재설정"


class AccountAdmin(UserAdmin):
	list_display = ('username', 'first_name', 'phone_number', 'email', 'date_joined', 'last_login', 'is_admin', 'is_staff')
	search_fields = ('username', 'email')
	readonly_fields = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('개인정보', {'fields': ('email', 'first_name', 'phone_number')}),
		('권한', {'fields': ('is_active', 'is_staff', 'is_admin')}),
		('중요 날짜', {'fields': ('last_login', 'date_joined')}),
	)

	actions = [reset_password_to_default]

admin.site.register(Account, AccountAdmin)
