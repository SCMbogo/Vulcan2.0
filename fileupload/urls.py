# encoding: utf-8
from django.conf.urls import url
from fileupload.views import (
        BasicVersionCreateView, PictureDeleteView, PictureListView,
        )

urlpatterns = [
    url(r'^basic/$', BasicVersionCreateView.as_view(), name='upload-basic'),
    url(r'^delete/(?P<pk>\d+)$', PictureDeleteView.as_view(), name='upload-delete'),
    url(r'^view/$', PictureListView.as_view(), name='upload-view'),
]
