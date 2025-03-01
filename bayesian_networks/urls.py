from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('challenge/<int:id>/<int:position>/', BayesianNetworkView.as_view(), name='challenge'),
    path('no-networks/', NoNetworksView.as_view(), name='no-networks'),
]
