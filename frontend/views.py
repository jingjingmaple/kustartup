from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from django.views import View




class SearchView(View):
	template_name = 'search.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name,{})

