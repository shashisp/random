from django.forms import ModelForm
from content.models import Content


class ContentForm(ModelForm):

	class Meta(ModelForm):
		model = Content
		fields = ('title', 'link', 'description', 'category')

	def __init__(self, *args, **kwargs):
		super(ContentForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs.update({'class' : 'form-control input', 'placeholder':'Nim Kathe'})
		self.fields['link'].widget.attrs.update({'class' : 'form-control', 'placeholder':'http://nimmcontentlink.com'})
		self.fields['description'].widget.attrs.update({'class' : 'form-control', 'placeholder':'Swalpa description'})
		self.fields['category'].widget.attrs.update({'class' : 'form-control'})		


	def clean(self):
		# import ipdb; ipdb.set_trace()
		pass