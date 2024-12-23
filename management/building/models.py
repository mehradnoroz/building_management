from django.db import models
import uuid


class Building(models.Model):
    
    class BuildingType(models.Choices):
        RESIDENTIAL = 'Residential', 'مسکونی'
        COMMERCIAL = 'Commercial', 'تجاری'
        OFFICE = 'Office', 'اداری'
        
    b_buildingtype=models.CharField(max_length=15,choices=BuildingType.choices,default=BuildingType.RESIDENTIAL)
    b_year_build=models.DateField()
    b_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    b_image = models.ImageField(upload_to='building_images/', null=True, blank=True)
    b_name=models.CharField(max_length=50)
    b_address=models.CharField(max_length=255)
    b_num_floor=models.PositiveIntegerField()
    b_num_of_units_in_every_floor=models.PositiveIntegerField()
    b_create_data_at=models.DateTimeField(auto_now_add=True)
    b_update_data_at=models.DateTimeField(auto_now=True)
    b_manager_name = models.CharField(max_length=100)
    b_manager_phone = models.CharField(max_length=15, blank=True, null=True)
    b_is_active = models.BooleanField(default=True)
    b_post_code=models.CharField(max_length=15,null=True,blank=True)
    b_security_manager_name = models.CharField(max_length=100, blank=True, null=True)
    b_security_manager_phone = models.CharField(max_length=15, blank=True, null=True)
    b_cost_charge_for_every_units=models.PositiveIntegerField(default=0)
    b_cost_buildings=models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.b_name
    
    # def b_cost_building(self):
    #     elevator_cost=self.elevatorss.first().e_cost_for_services_monthly if self.elevatorss.exists() else 0
    #     building_cost=self.b_num_floor*self.b_num_of_units_in_every_floor*self.b_cost_charge_for_every_units
    #     total_cost=elevator_cost+building_cost
    #     return total_cost
class Meeting(models.Model):
    building = models.ForeignKey('Building', on_delete=models.CASCADE,related_name='meeting')
    date=models.DateTimeField()
    agenda = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.building} جلسات ساختمان"
    




    
    
