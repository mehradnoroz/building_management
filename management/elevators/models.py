from django.db import models
import uuid


class Elevators(models.Model):
    e_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    e_building=models.ForeignKey('building.Building',on_delete=models.CASCADE,related_name='elevatorss')
    e_is_active=models.BooleanField(default=True)
    e_maintenance_date_services= models.DateField(null=True, blank=True)
    e_manufacturer = models.CharField(max_length=100, null=True, blank=True)
    e_email_manufacturer=models.EmailField(null=True,blank=True)
    e_send_message_with_email=models.BooleanField(default=False)
    e_phone_manufacturer=models.CharField(max_length=13,null=True,blank=True)
    e_send_message_with_sms=models.BooleanField(default=False)
    e_telephone_manufacturer=models.CharField(max_length=11,null=True,blank=True)
    e_text_for_send_with_email_or_sms=models.TextField(null=True,blank=True)
    e_cost_for_services_monthly=models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'{self.e_building} آسانسور ساختمان'
