from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


from django.views.generic import ListView
import content.models as models
from content.forms import ContentForm, VoteForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from django.views.generic.edit import FormView
from django.views.generic import DetailView
from datetime import date

class ContentListView(ListView):
	model = models.Content
	queryset = models.Content.with_votes.filter(submitted_on=date.today())


class ContentDetailView(DetailView):
    model = models.Content
   

@login_required(login_url='/login/')
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
        	submitted_by = request.user
        	content = models.Content.objects.create(title=title, description=description,
        				link=link, category=category, submitted_by=submitted_by)
        	return HttpResponseRedirect('/')
 
    return render(request, 'content/add_content.html', {
        'form': form,
    })

class VoteFormView(FormView):
    form_class = VoteForm


    def form_valid(self, form):
        content = get_object_or_404(models.Content, pk=form.data["content"])
        user = self.request.user
        prev_vote = models.Vote.objects.filter(content=content, voter=user)
        has_voted = prev_vote.count() > 0

        if not has_voted:
            models.Vote.objects.create(content=content, voter=user)
            # import ipdb; ipdb.set_trace()
            print "voted"
        else:
            prev_vote[0].delete()

        return HttpResponseRedirect('/')

def collections(request):
    return render(request, 'collections.html')



def login(request):
	return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/')
