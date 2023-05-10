from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.validators import RegexValidator
from autoslug import AutoSlugField

slug_validator = RegexValidator(
    r'^[가-힣A-Za-z0-9_-]+$',
    'Only Korean letters, alphanumeric, hyphen, and underscore characters are allowed.'
)


def upload_location(instance, filename):
	file_path = 'announce/{author_id}/{title}-{filename}'.format(
				author_id=str(instance.author.id),title=str(instance.title), filename=filename)
	return file_path


class BlogPost(models.Model):
	class Meta:
		verbose_name = '공지사항'
		verbose_name_plural = '공지사항'
	title 					= models.CharField(verbose_name='제목', max_length=70, null=False, blank=False)
	body 					= models.TextField(verbose_name='내용', max_length=50000, null=False, blank=False)
	image		 			= models.ImageField(verbose_name='사진', upload_to=upload_location, null=True, blank=True)
	date_published 			= models.DateTimeField(auto_now_add=True, verbose_name="업로드 일짜")
	date_updated 			= models.DateTimeField(auto_now=True, verbose_name="마지막 업데이트")
	author 					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자', related_name='announce_blog_posts')
	slug 					= AutoSlugField(populate_from='title', unique=True, validators=[slug_validator])

	def __str__(self):
		return self.title


@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 

def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.author.first_name + "-" + instance.title)

pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)