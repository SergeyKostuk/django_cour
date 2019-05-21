from django.urls import path
from cw19.views import record


urlpatterns = [

    path('record/', record),


]
