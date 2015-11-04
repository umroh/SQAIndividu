from django.conf.urls import include, url
from lists import views
#from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', views.home_page, name='home'),
    #url(r'^admin/', include(admin.site.urls)),
]
