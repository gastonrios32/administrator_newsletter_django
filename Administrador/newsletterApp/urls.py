from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required

urlpatterns = [
path('',login_required(views.postList.as_view()), name="inicio" ),
path('tags/',login_required(views.tagList.as_view()), name="tags_list" ),

path('post_new/',login_required(views.postnew.as_view()), name="new_post" ),
path('tag_new/',login_required(views.tagsnew.as_view()), name="new_tag" ),
path('comment_new/',login_required(views.Commentnew.as_view()), name="comment_new" ),

path('post_update/<int:id_post>/',login_required(views.postUpdate.as_view()), name="post_update" ),
path('tags_Update/<int:id_tag>/',login_required(views.tagsUpdate.as_view()), name="tags_Update" ),
path('comment_Update/<int:id>/',login_required(views.commentUpdate.as_view()), name="comment_Update" ),

path('post_delete/<int:id_post>/',login_required(views.postdelete.as_view()), name="post_delete" ),
path('tags_delete/<int:id_tag>/',login_required(views.tagsdelete.as_view()), name="tags_delete" ),
path('comment_delete/<int:id>/',login_required(views.commentdelete.as_view()), name="comment_delete" ),

path('postdetail/<int:id_post>/',login_required(views.postDetail.as_view()), name="post_detail" ),

path('accounts/login/', LoginView.as_view(template_name = 'newsletterApp/login.html'), name="login" ),
path('logout/', logout_then_login, name="logout" ),
#path('logout/', LogoutView.as_view(), {'template_name': 'newsletterApp/logged_out.html'}, name = 'logout'),


]