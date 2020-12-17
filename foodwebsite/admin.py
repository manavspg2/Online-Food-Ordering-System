from django.contrib import admin

from .models import *

class FoodItemsAdmin(admin.ModelAdmin):
	model = FoodItems
	list_display = ['name','get_name']

	def get_name(self,obj):
		return obj.rest.name
	get_name.short_description = 'Restaurant'


admin.site.register(FoodItems, FoodItemsAdmin)
admin.site.register(Restaurant)
admin.site.register(CurrentOrders)
admin.site.register(Customer)
admin.site.register(OrderHistory)
admin.site.register(Reviews)
