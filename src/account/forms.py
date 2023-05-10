from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm
from account.models import Account

class RegisterationForm(UserCreationForm):
	email = forms.EmailField(label='이메일', max_length=60, error_messages = {'invalid': '올바른 이메일 주소를 입력해주세요.'})
	first_name = forms.CharField(label='이름', max_length=15)
	phone_number = forms.CharField(label='휴대전화', max_length=20, help_text='숫자만 입력해주세요. 예 : 01011112222', error_messages = {'invalid': '숫자만 입력해주세요.'})
	password1 = forms.CharField(label="비밀번호", widget=forms.PasswordInput())
	password2 = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput())

	class Meta:
		model = Account
		fields = ("username", "email", "first_name", "phone_number", "password1", "password2")

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
		return password2

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if Account.objects.filter(username=username).exists():
			raise forms.ValidationError("존재하는 아이디 입니다.")
		return username

	def clean_phone_number(self):
		phone_number = self.cleaned_data.get('phone_number')
		if len(phone_number) > 11:
			raise forms.ValidationError("휴대전화 번호는 11자리 이하여야 합니다.")
		return phone_number




class AccountAuthenticationForm(forms.ModelForm):
	password = forms.CharField(label="비밀번호", widget=forms.PasswordInput())

	class Meta:
		model = Account
		fields = ('username', 'password')

	def clean(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			password = self.cleaned_data['password']
			if not authenticate(username=username, password=password):
				raise forms.ValidationError("아이디/비밀번호를 확인해주세요.")


class AccountUpdateForm(forms.ModelForm):
    username = forms.CharField(label='아이디', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    password = forms.CharField(label='현재 비밀번호', widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))
    new_password = forms.CharField(label='새로운 비밀번호', widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))

    class Meta:
        model = Account
        fields = ('username', 'password', 'new_password')

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not self.instance.check_password(password):
            raise forms.ValidationError("현재 비밀번호가 올바르지 않습니다.")
        return password


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        new_password = cleaned_data.get("new_password")

        if password and new_password:
            if password == new_password:
                raise forms.ValidationError("새 비밀번호가 이전 비밀번호와 동일합니다.")
