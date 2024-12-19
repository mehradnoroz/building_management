from django.db import models
import uuid


class Elevators(models.Model):
    e_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    e_building=models.ForeignKey('Building',on_delete=models.CASCADE,related_name='elevators')
    e_is_active=models.BooleanField(default=True)
    e_maintenance_date = models.DateField(null=True, blank=True)
    e_manufacturer = models.CharField(max_length=100, null=True, blank=True)
    e_email_manufacturer=models.EmailField()
    e_telephone_manufacturer=models.TextField()
    
    

    def __str__(self):
        return f'{self.e_building}آسانسور ساختمان'
