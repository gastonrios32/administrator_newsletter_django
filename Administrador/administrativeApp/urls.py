from django.urls import path
from . import views
urlpatterns = [
path('',views.inicio, name = 'inicio'),
path('members/',views.membersList.as_view(), name="members" ),
path('memberdetail/<int:id_member>/',views.memberDetail.as_view(), name="member_detail" ), 
path('membernew/',views.membernew.as_view(), name="new_member" ),
path('member_detail_new/',views.memberdetailnew.as_view(), name="new_member_detail" ),
path('member_Job_new/',views.MemberJobnew.as_view(), name="new_Member_Job" ),
path('member_phone_new/',views.Memberphonenew.as_view(), name="new_Member_phone" ),
path('member_email_new/',views.MemberEmailnew.as_view(), name="new_Member_email" ),
]