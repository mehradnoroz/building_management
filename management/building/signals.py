from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Building
from elevators.models import Elevators


@receiver(post_save,sender=Building)
def when_updating_b_cost_charge_for_every_units_then_update_b_cost_building(sender,instance,created,**kwargs):
    try:
        elevator_cost=0
        elevator=Elevators.objects.get(e_building=instance)
        elevator_cost=elevator.e_cost_for_services_monthly
    except Elevators.DoesNotExist:
        elevator_cost=0  
          
    building_cost=instance.b_num_of_units_in_every_floor * instance.b_num_floor * instance.b_cost_charge_for_every_units
    total_cost=elevator_cost + building_cost
    instance.b_cost_buildings=total_cost
    Building.objects.filter(pk=instance.pk).update(b_cost_buildings=total_cost)


@receiver(post_save,sender=Elevators)
def when_updating_e_cost_for_services_monthly_then_update_b_cost_building(sender,instance,created,**kwargs):
    building_cost=instance.e_building.b_num_of_units_in_every_floor * instance.e_building.b_num_floor * instance.e_building.b_cost_charge_for_every_units
    elevator_cost=instance.e_cost_for_services_monthly
    total_cost=building_cost+elevator_cost
    instance.e_building.b_cost_buildings=total_cost
    Building.objects.filter(pk=instance.e_building.pk).update(b_cost_buildings=total_cost)
    