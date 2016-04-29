from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

	url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset', {'template_name' : 'user/password/password_reset.html'},
			name='password_reset'),
    
    url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done',
    	{'template_name' : 'user/password/password_reset_done.html'}, name = 'password_reset_done'),
    
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', 
    	{'template_name' : 'user/password/password_reset_confirm.html' }, name ='password_reset_confirm'),
    
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete',
    	{'template_name' : 'user/password/password_reset_complete.html' }, name ='password_reset_complete'),

    url(r'^change-password/$', 'django.contrib.auth.views.password_change',
    	{'template_name' : 'user/password/password_change.html' }, name="password_change"),

	url(r'^change-password-done/$', 'django.contrib.auth.views.password_change_done',
		{'template_name' : 'user/password/password_change_done.html' }, name="password_change_done"),

	url(r'^', include('app.web.urls')),
    #url(r'^manager/', include('app.manager.urls')),
    url(r'^user/', include('app.user.urls')),
    url(r'^admin/', include(admin.site.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG is False:
	urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	)
