from django.conf.urls import url
from .views import Profile, ProfileUpdate, PasswordUpdateView, Login, RegisterView

urlpatterns = [
	
	url(r'^login/$', Login.as_view(), name = 'login'),
    url(r'^register/$', RegisterView.as_view(), name = 'register'),
    url(r'^logout/$', Login.logout, name = 'logout'),

	url(r'^profile/$', Profile.as_view(), name = 'profile'),
	url(r'^update/(?P<pk>[0-9]+)/$', ProfileUpdate.as_view(), name = 'profile_update'),
	url(r'^password/(?P<pk>[0-9]+)/$', PasswordUpdateView.as_view(), name = 'password_update'),

]