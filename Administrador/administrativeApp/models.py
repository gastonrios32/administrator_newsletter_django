
from django.db import models

# Create your models here.

class TlbJobPosition(models.Model):
    id_position = models.AutoField(primary_key=True)
    desc_position = models.CharField(db_column='Desc_position', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tlb_job_Position'
        
    def __str__(self):
        return f'{self.id_position} - {self.desc_position}'


class TlbMemberDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    #id_member = models.ForeignKey('TlbMembers', models.DO_NOTHING, db_column='id_member', blank=True, null=True)
    id_member = models.ForeignKey('TlbMembers', on_delete=models.CASCADE,db_column='id_member')    
    date_bith = models.DateField('Fecha de Nacimiento',blank= False , null=False)
    direction = models.CharField(max_length=250, blank=True, null=True)
    #civil_status = models.ForeignKey('TlbStatusCivil', models.DO_NOTHING, db_column='Civil_status')  # Field name made lowercase.
    civil_status = models.ForeignKey('TlbStatusCivil', on_delete=models.CASCADE,db_column='Civil_status')  # Field name made lowercase.    
    dependents = models.IntegerField(db_column='Dependents', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tlb_member_detail'
        ordering = ['id_member']
    
    def __str__(self):
        return f'{self.detail_id} - {self.id_member} - {self.date_bith} - {self.direction} - {self.civil_status} - {self.dependents}'


class TlbMemberEmail(models.Model):
    id_email = models.AutoField(primary_key=True)
    #id_member = models.ForeignKey('TlbMembers', models.DO_NOTHING, db_column='id_member')
    id_member = models.ForeignKey('TlbMembers', on_delete=models.CASCADE,db_column='id_member')    
    email = models.EmailField(max_length=254, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'tlb_member_email'
    
    def __str__(self):
        return f'{self.id_email} - {self.id_member} - {self.email} '


class TlbMemberJob(models.Model):
    job_id = models.AutoField(db_column='Job_ID', primary_key=True)  # Field name made lowercase.
    #id_member = models.ForeignKey('TlbMembers', models.DO_NOTHING, db_column='id_member', blank=True, null=True)
    id_member = models.ForeignKey('TlbMembers', on_delete=models.CASCADE,db_column='id_member')    
    #id_position = models.ForeignKey(TlbJobPosition, models.DO_NOTHING, db_column='id_position', blank=True, null=True)
    id_position = models.ForeignKey(TlbJobPosition, on_delete=models.CASCADE,db_column='id_position')    
    date_entry = models.DateField('Fecha de Ingreso',blank= False , null=False)
    direction = models.CharField(max_length=250, blank=True, null=True)
    job_name = models.CharField(db_column='Job_name', max_length=150, blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'tlb_member_job'
        ordering = ['id_member']
    
    def __str__(self):
        return f'{self.job_id} - {self.id_member} - {self.id_position} - {self.date_entry} - {self.direction}  - {self.job_name}  '    


class tlb_member_phone(models.Model):
    id_contact = models.AutoField(primary_key=True)
    #id_member = models.ForeignKey('TlbMembers', models.DO_NOTHING, db_column='id_member')
    id_member = models.ForeignKey('TlbMembers', on_delete=models.CASCADE,db_column='id_member')    
    phone1 = models.CharField(db_column='Phone1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type_phone = models.CharField(max_length=50, blank=True, null=True)
    status_fone = models.IntegerField(blank=True, null=True,default= 1)

    class Meta:
        managed = True
        db_table = 'tlb_member_phone'

    def __str__(self):
        return f'{self.id_contact} - {self.id_member} - {self.phone1} - {self.type_phone} - {self.status_fone}  '    


class TlbMembers(models.Model):
    id_member = models.IntegerField(primary_key=True)
    member_name = models.CharField(max_length=100)
    status_memb = models.IntegerField(default= 1)
    create_at = models.DateField (auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = 'tlb_members'
        ordering = ['id_member']

    def __str__(self):
        return f'{self.id_member} - {self.member_name} '    


class TlbStatusCivil(models.Model):
    id_civilstatus = models.AutoField(primary_key=True)
    desc_civil = models.CharField(db_column='Desc_civil', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tlb_status_Civil'

    def __str__(self):
        return f'{self.id_civilstatus} - {self.desc_civil}'    
        