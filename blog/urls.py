from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),

    #hiçbişey yazmazsa viewin altındaki post_list methodunu çağır

]
