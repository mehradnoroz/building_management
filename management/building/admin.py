from django.contrib import admin
from .models import Building,Meeting
from django.utils.html import format_html


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display=('show_image','b_name','b_buildingtype',)
    list_display_links=("b_name","show_image")
    list_per_page=2
    list_max_show_all=3
    
    def show_image(self, obj):
        if obj.b_image:  
            return format_html('<img src="{}" style="max-width:200px; max-height:200px;" />', obj.b_image.url)
        return "No Image"
    
    show_image.allow_tags = True
    show_image.short_description = 'Picture'
    
    
    
admin.site.register(Meeting)
        
