from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.ResumeListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<pk>[0-9]+)/$',
        view=views.ResumeDetailView.as_view(),
        name='resume_detail'
    )
]
