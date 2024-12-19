from django.db import models
import uuid



class Building(models.Model):
    
    class BuildingType(models.Choices):
        RESIDENTIAL = 'Residential', 'مسکونی'
        COMMERCIAL = 'Commercial', 'تجاری'
        OFFICE = 'Office', 'اداری'
        
    buildingtype=models.CharField(max_length=15,choices=BuildingType.choices,default=BuildingType.RESIDENTIAL)
    b_year_build=models.DateField()
    b_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    b_image = models.ImageField(upload_to='building_images/', null=True, blank=True)
    b_name=models.CharField(max_length=50)
    b_address=models.CharField(max_length=255)
    b_num_floor=models.IntegerField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    b_manager_name = models.CharField(max_length=100)
    b_manager_phone = models.CharField(max_length=15, blank=True, null=True)
    b_is_active = models.BooleanField(default=True)
    has_active_elevator=models.BooleanField(default=True)
    b_post_code=models.CharField(max_length=15,null=True,blank=True)
    security_manager_name = models.CharField(max_length=100, blank=True, null=True)
    security_manager_phone = models.CharField(max_length=15, blank=True, null=True)

    # def update_elevator_status(self):
    #     self.has_active_elevator=self.elevators.filter(e_is_active=True).exists()
    #     self.save()
        
    def __str__(self):
        return self.b_name
    
class Meeting(models.Model):
    building = models.ForeignKey('Building', on_delete=models.CASCADE,related_name='meeting')
    date=models.DateTimeField()
    agenda = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.building} جلسات ساختمان"
    




    
    
