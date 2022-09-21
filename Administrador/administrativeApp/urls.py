from django.urls import path
from . import views
urlpatterns = [
path('',views.inicio_administrador, name = 'inicio_administrador'),

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
path('member_job_update/<int:job_id>/',views.MemberJobUpdate.as_view(), name="member_job_update" ),
path('member_phone_update/<int:id_contact>/',views.MemberPhoneUpdate.as_view(), name="member_phone_update" ),
path('member_email_update/<int:id_email>/',views.MemberEmailUpdate.as_view(), name="member_email_update" ),

#DELETEVIEW
path('member_delete/<int:id_member>/',views.memberdelete.as_view(), name="member_delete" ),
path('member_job_delete/<int:job_id>/',views.memberJobdelete.as_view(), name="member_job_delete" ),
path('member_phone_delete/<int:id_contact>/',views.memberPhonedelete.as_view(), name="member_phone_delete" ),
path('member_email_delete/<int:id_email>/',views.memberEmaildelete.as_view(), name="member_email_delete" ),
]