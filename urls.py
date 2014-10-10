from django.conf.urls import url, patterns
from {{ app_name }} import views

urlpatterns = patterns(
    "",
    url(ur"$^", views.IdentityHome.as_view(), name="{{ app_name }}-home")
)
