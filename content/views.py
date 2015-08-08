from django.shortcuts import render
from django.views.generic import ListView
import content.models as models


class ContentListView(ListView):
	model = models.Content
	queryset = models.Content.with_votes.all()