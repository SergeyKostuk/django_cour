
from django.urls import path

from myapp2.views import len_of_coment
from myapp2.views import text_area

urlpatterns = [

    path('count/', len_of_coment),
    path('textarea/', text_area),

]