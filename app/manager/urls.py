from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^home/$', ManagerHomeView.as_view(), name = 'manager_home'),
	#url(r'^profile/$', ManagerProfileView.as_view(), name = 'manager_profile'),
	#url(r'^password/(?P<pk>[0-9]+)/$', ManagerPasswordChangeView.as_view(), name = 'manager_password'),

	url(r'^rank/$', RankListView.as_view(), name = 'manager_rank'),
	url(r'^competition/$', CompetitionListView.as_view(), name = 'manager_competition'),

	url(r'^rank/create/$', RankCreateView.as_view(), name = 'manager_rank_create'),
	url(r'^competition/create/$', CompetitionCreateView.as_view(), name = 'manager_competition_create'),

	url(r'^rank/update/(?P<pk>[0-9]+)/$', RankUpdateView.as_view(), name = 'manager_rank_update'),
	url(r'^competition/update/(?P<pk>[0-9]+)/$', CompetitionUpdateView.as_view(), name = 'manager_competition_update'),
	
	url(r'^login/$', ManagerLoginView.as_view(), name = 'manager_login'),
	url(r'^logout/$', ManagerLoginView.logout, name = 'manager_logout'),
	url(r'^rank_create/$', RankCreateExample.as_view(), name = 'manager_rank_create_example')
]