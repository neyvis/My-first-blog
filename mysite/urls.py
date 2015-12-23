from django.conf.urls import include, url
from django.contrib import admin

#from blog.views import blog_index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', blog_index),
    url(r'', include('blog.urls')),
]

#urlpatterns = [
    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
#]#
