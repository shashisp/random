from django.shortcuts import render
from django.views.generic import ListView
import content.models as models
from content.forms import ContentForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout

class ContentListView(ListView):
	model = models.Content
	queryset = models.Content.with_votes.all()



def add_new(request):
    if request.method == 'GET':
        form = ContentForm()
    else:
        
        form = ContentForm(request.POST)
        
        if form.is_valid():
        	title = form.cleaned_data['title']
        	link = form.cleaned_data['link']
        	description = form.cleaned_data['description']
        	category = form.cleaned_data['category']
        	submitted_by = User.objects.get(id=1)
        	content = models.Content.objects.create(title=title, description=description,
        				link=link, category=category, submitted_by=submitted_by)
        	return HttpResponseRedirect('/')
 
    return render(request, 'content/add_content.html', {
        'form': form,
    })