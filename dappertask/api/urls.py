from django.conf.urls import url
from django.urls import include

from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

import api.views as dv

router = DefaultRouter(trailing_slash=False)
app_router = routers.DefaultRouter()

urlpatterns = [

    # documentation
    url(r'^docs/', include_docs_urls(title='Dappertask Backend API', public=True)),
    # url(r'^auth/', include('rest_framework_social_oauth2.urls')),

    # User management and registration urls
    url('accounts/', include('rest_registration.api.urls')),

    # tontine urls
    url(r'^api/', include(app_router.urls)),
    # url(regex=r'^tontine/addmember/$',view=tv.AddMemberAndTontine.as_view(),name='addmember'),

]
