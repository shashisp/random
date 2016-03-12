from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True, null=True)
	twitter_handle = models.CharField(max_length=150)
	twitter_image = models.URLField()

	def __unicode__(self):
		return self.user.first_name


def social_auth_to_profile(backend, details, response, user=None, is_new=False, *args, **kwargs):
	if is_new:
		profile = UserProfile.objects.get_or_create(user=user)
		profile[0].twitter_image = response['profile_image_url_https']
		profile[0].twitter_handle = response['screen_name']
		profile[0].save()
	else:
		profile = UserProfile.objects.get_or_create(user=user)
		profile.save()


