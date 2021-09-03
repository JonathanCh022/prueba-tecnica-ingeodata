from django.urls import path
from ingeodata_pruebatecnica.apps.postApp.views import MyFormView

urlpatterns = [
    path('save', MyFormView.as_view(), name='myformAPI'),
    path('show', MyFormView.as_view(), name='myformAPI'),
]