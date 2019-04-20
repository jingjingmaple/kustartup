from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required


from . import views
app_name = 'adminDashboard'
urlpatterns = [
	path('', views.SearchView.as_view(), name='search'),
	
	
]