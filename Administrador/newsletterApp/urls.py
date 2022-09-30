from django.urls import path
from . import views
urlpatterns = [
path('',views.postList.as_view(), name="inicio" ),

path('post_new/',views.postnew.as_view(), name="new_post" ),
path('post_update/<int:id_post>/',views.postUpdate.as_view(), name="post_update" ),
path('post_delete/<int:id_post>/',views.postdelete.as_view(), name="post_delete" ),
path('postdetail/<int:id_post>/',views.postDetail.as_view(), name="post_detail" ),


]