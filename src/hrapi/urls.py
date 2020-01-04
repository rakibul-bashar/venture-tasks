from django.conf.urls import url
from .views import (
    ProjectListView,
    ProjectDetailsView,
    LogListView,
    LogDetailsView,
)

urlpatterns = [
    url('^project/$', ProjectListView.as_view(), name='project'),
    url('^project/(?P<id>\d+)/$', ProjectDetailsView.as_view(), name='project_update_delete'),
    url('^log/$', LogListView.as_view(), name='log'),
    url('^log/(?P<id>\d+)/$', LogDetailsView.as_view(), name='log_update_delete'),

]