from django.conf.urls import url
from . import views

urlpatterns = [
    #path('',views.post_list,name='post_list'),
    url(r'^hkmanagement/add-asset/',views.add_asset,name='add_asset'),
    url(r'^hkmanagement/add-task/',views.add_task,name='add_task'),
    url(r'^hkmanagement/add-worker/',views.add_worker,name='add_worker'),
    url(r'^hkmanagement/assets/all/',views.display_assets,name='display_assets'),
    url(r'^hkmanagement/allocate-task/',views.allocate_task,name='allocate_task'),
    url(r'^hkmanagement/get-tasks-for-worker/(?P<pk>\d+)/$',views.get_tasks_for_worker,name='get_tasks_for_worker'),
]