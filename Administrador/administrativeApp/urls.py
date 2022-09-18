from django.urls import path
from . import views
urlpatterns = [
path('',views.inicio, name = 'inicio'),

#LISTVIEW
path('members/',views.membersList.as_view(), name="members" ),
path('memberdetail/',views.memberDetailList.as_view(), name="member_detail_list" ),
path('memberjob/',views.memberjobList.as_view(), name="member_job_list" ),
path('memberphone/',views.memberphoneList.as_view(), name="member_phone_list" ),
path('memberemail/',views.memberemailList.as_view(), name="member_email_list" ),

#DETAILVIEW
path('memberdetail/<int:id_member>/',views.memberDetail.as_view(), name="member_detail" ),
path('memberdetail_job/<int:id_member>/',views.memberDetail_job.as_view(), name="member_detail_job" ),
path('memberdetail_phone/<int:id_member>/',views.memberDetail_phone.as_view(), name="member_detail_phone" ),
path('memberdetail_email/<int:id_member>/',views.memberDetail_email.as_view(), name="member_detail_email" ),

#CREATEVIEW 
path('membernew/',views.membernew.as_view(), name="new_member" ),
path('member_detail_new/',views.memberdetailnew.as_view(), name="new_member_detail" ),
path('member_Job_new/',views.MemberJobnew.as_view(), name="new_Member_Job" ),
path('member_phone_new/',views.Memberphonenew.as_view(), name="new_Member_phone" ),
path('member_email_new/',views.MemberEmailnew.as_view(), name="new_Member_email" ),

#UPDATEVIEW

path('member_update/<int:id_member>/',views.MemberUpdate.as_view(), name="member_update" ),
path('member_detail_update/<int:id_member>/',views.MemberDetailUpdate.as_view(), name="member_detail_update" ),
path('member_job_update/<int:id_member>/',views.MemberJobUpdate.as_view(), name="member_job_update" ),
path('member_phone_update/<int:id_member>/',views.MemberPhoneUpdate.as_view(), name="member_phone_update" ),
path('member_email_update/<int:id_member>/',views.MemberEmailUpdate.as_view(), name="member_email_update" ),

#DELETEVIEW

]