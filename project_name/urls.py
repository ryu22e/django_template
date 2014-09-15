from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from home.views import HomeView

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', HomeView.as_view(), name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
    )
