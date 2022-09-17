from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(TlbMembers)
admin.site.register(TlbMemberDetail)
admin.site.register(TlbJobPosition)
admin.site.register(TlbMemberEmail)
admin.site.register(TlbMemberJob)
admin.site.register(tlb_member_phone)
admin.site.register(TlbStatusCivil)

