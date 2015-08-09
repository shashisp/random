from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

class LinkVoteCountManager(models.Manager):

    def get_query_set(self):
        return super(LinkVoteCountManager, self).get_query_set().annotate(
            votes=Count('vote')).order_by('-votes')


class Content(models.Model):
	ARTICLE = 0
	VIDEO = 1
	MUSIC = 2
	BOOK = 3
	SERVICE_CHOICES = (
    	(ARTICLE, "Article"),
    	(VIDEO, "Video"),
    	(MUSIC, "Music"),
    	(BOOK, "Book"),
    )
	title = models.CharField(max_length=100)
	link = models.URLField(max_length=100)
	submitted_by = models.ForeignKey(User)
	submitted_on = models.DateTimeField(auto_now_add=True)
	description = models.TextField(blank=True)
	category = models.IntegerField(choices=SERVICE_CHOICES, default=None)
	with_votes = LinkVoteCountManager()
	objects = models.Manager() 

	def __unicode__(self):
		return self.title


class Vote(models.Model):
	content = models.ForeignKey(Content)
	voter = models.ForeignKey(User)

	def __unicode__(self):
		return "%s upvoted %s" % (self.voter, self.content.title)
