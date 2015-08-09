from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
import content.models as models


class ContentListView(ListView):
	model = models.Content
	queryset = models.Content.with_votes.all()


@login_required(login_url='/login/')
def add_content(request):
	pass


def login(request):
	return render(request, 'login.html')



def logout(request):
    auth_logout(request)
    return redirect('/')