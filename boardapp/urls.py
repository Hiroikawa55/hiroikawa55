from django.urls import path
from .views import signupfunc, loginfunc, logoutfunc, detailfunc, goodfunc, readfunc, find, BoardEdit, near, others, listfunc
# from .views import Listview, BoardCreate

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    # path('list/', Listview.as_view(), name='list'),
    path('list/', listfunc, name='list'),
    path('list/<int:num>', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
    # path('create/', BoardCreate.as_view(), name='create'),
    path('find/', find, name='find'),
    path('find/<int:num>', find, name='find'),
    path('others/', others, name='others'),
    path('others/<int:num>', others, name='others'),
    path('near/', near, name='near'),
    path('near/<int:num>', near, name='near'),
    path('near/', near, name='near'),
    path('edit/<int:pk>', BoardEdit.as_view(), name='edit'),
]