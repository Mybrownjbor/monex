from django.conf.urls import url
from .views import ManagerLoginView, ManagerHomeView, ManagerProfileView, ManagerPasswordChangeView

urlpatterns = [
	url(r'^home/$', ManagerHomeView.as_view(), name = 'manager_home'),
	url(r'^profile/$', ManagerProfileView.as_view(), name = 'manager_profile'),
	url(r'^password/(?P<pk>[0-9]+)$', ManagerPasswordChangeView.as_view(), name = 'manager_password'),
	
	url(r'^login/$', ManagerLoginView.as_view(), name = 'manager_login'),
	url(r'^logout/$', ManagerLoginView.logout, name = 'manager_logout'),
]