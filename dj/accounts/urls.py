#  accounts/views.py

from django.conf.urls import url, patterns

from accounts.views import logax

# django-registration default urls
urlpatterns = patterns(
    '',
    url(r'^login/$',
        logax,
        name='auth_login',
        ),

)

