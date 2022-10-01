from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
path('',login_required(views.administrador.as_view()), name = 'inicio_administrador'),


#LISTVIEW
path('members/',login_required(views.membersList.as_view()), name="members" ),
path('memberdetail/',login_required(views.memberDetailList.as_view()), name="member_detail_list" ),
path('memberjob/',login_required(views.memberjobList.as_view()), name="member_job_list" ),
path('memberphone/',login_required(views.memberphoneList.as_view()), name="member_phone_list" ),
path('memberemail/',login_required(views.memberemailList.as_view()), name="member_email_list" ),

#DETAILVIEW
path('memberdetail/<int:id_member>/',login_required(views.memberDetail.as_view()), name="member_detail" ),
path('memberdetail_job/<int:id_member>/',login_required(views.memberDetail_job.as_view()), name="member_detail_job" ),
path('memberdetail_phone/<int:id_member>/',login_required(views.memberDetail_phone.as_view()), name="member_detail_phone" ),
path('memberdetail_email/<int:id_member>/',login_required(views.memberDetail_email.as_view()), name="member_detail_email" ),

#CREATEVIEW 
path('membernew/',login_required(views.membernew.as_view()), name="new_member" ),
path('member_detail_new/',login_required(views.memberdetailnew.as_view()), name="new_member_detail" ),
path('member_Job_new/',login_required(views.MemberJobnew.as_view()), name="new_Member_Job" ),
path('member_phone_new/',login_required(views.Memberphonenew.as_view()), name="new_Member_phone" ),
path('member_email_new/',login_required(views.MemberEmailnew.as_view()), name="new_Member_email" ),

#UPDATEVIEW

path('member_update/<int:id_member>/',login_required(views.MemberUpdate.as_view()), name="member_update" ),
path('member_detail_update/<int:id_member>/',login_required(views.MemberDetailUpdate.as_view()), name="member_detail_update" ),
path('member_job_update/<int:job_id>/',login_required(views.MemberJobUpdate.as_view()), name="member_job_update" ),
path('member_phone_update/<int:id_contact>/',login_required(views.MemberPhoneUpdate.as_view()), name="member_phone_update" ),
path('member_email_update/<int:id_email>/',login_required(views.MemberEmailUpdate.as_view()), name="member_email_update" ),

#DELETEVIEW
path('member_delete/<int:id_member>/',login_required(views.memberdelete.as_view()), name="member_delete" ),
path('member_job_delete/<int:job_id>/',login_required(views.memberJobdelete.as_view()), name="member_job_delete" ),
path('member_phone_delete/<int:id_contact>/',login_required(views.memberPhonedelete.as_view()), name="member_phone_delete" ),
path('member_email_delete/<int:id_email>/',login_required(views.memberEmaildelete.as_view()), name="member_email_delete" ),
]