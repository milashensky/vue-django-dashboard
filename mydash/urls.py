from django.urls import path, re_path, include
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from common.auth import LoginView, LogoutView


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name='logout'),
    path('', include(('common.urls', 'common'), namespace='common')),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += staticfiles_urlpatterns()

if getattr(settings, "DEBUG_TOOLBAR", None):
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
