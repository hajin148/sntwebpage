from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, first_name, phone_number, password=None):
		if not email:
			raise ValueError("이메일을 입력해주세요.")
		if not username:
			raise ValueError("아이디를 입력해주세요.")
		if not first_name:
			raise ValueError("이름을 입력해주세요.")
		if not phone_number:
			raise ValueError("전화번호를 입력해주세요.")

		user = self.model(
			email = self.normalize_email(email),
			username=username,
			first_name=first_name,
			phone_number=phone_number
			)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, first_name, phone_number, username, password):
		user = self.model(
			email = self.normalize_email(email),
			username=username,
			first_name=first_name,
			phone_number=phone_number
			)
		user.is_admin=True
		user.is_staff=True
		user.is_superuser=True

		user.set_password(password)
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
	class Meta:
		verbose_name = '회원정보'
		verbose_name_plural = '회원정보'
	email 				= models.EmailField(verbose_name='이메일', max_length=60, unique=True)
	username 			= models.CharField(verbose_name='아이디', max_length=30, unique=True)
	date_joined			= models.DateTimeField(verbose_name='회원가입일', auto_now_add=True)
	last_login 			= models.DateTimeField(verbose_name='마지막로그인', auto_now=True)
	is_admin 			= models.BooleanField(verbose_name='어드민계정', default=False)
	is_staff			= models.BooleanField(verbose_name='스태프계정', default=False)
	is_superuser		= models.BooleanField(default=False)
	is_active 			= models.BooleanField(verbose_name='활성화계정', default=True)
	first_name			= models.CharField(verbose_name="이름", max_length=30)
	phone_number		= models.CharField(verbose_name="휴대번호", max_length=11)


	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'first_name', 'phone_number']

	objects = MyAccountManager()

	def __str__(self):
		return self.username 
		# return self.email + ", " + self.username

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True