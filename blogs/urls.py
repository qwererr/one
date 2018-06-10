# @Time    : 18-6-5 下午2:19
# @Author  :
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from .views import index
from .views import Search
from .views import list
from .views import bq
urlpatterns = [

    url(r'^index/$', index, name='index'),
    url(r'^search/$', Search.as_view(), name='search'),
    url(r'^list/$', list, name='list'),
    url(r'^bq/(?P<q>[0-9]+)/$',bq,name='bq'),



    

]

