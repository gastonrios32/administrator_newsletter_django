from django.urls import path
from . import views
urlpatterns = [
path('',views.inicio, name = 'inicio'),
path('members/',views.membersList.as_view(), name="members" ),
path('memberdetail/<fk>/',views.memberDetail.as_view(), name="member_detail" ), 
path('membernew/',views.membernew.as_view(), name="new_member" ),
path('member_detail_new/',views.memberdetailnew.as_view(), name="new_member_detail" ),

]