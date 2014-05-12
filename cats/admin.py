from django.contrib import admin
from models import *


class OpeningHoursInline(admin.TabularInline):
	model = OpeningHours
	extra = 6


class CatProfileAdmin(admin.ModelAdmin):
	list_display = ['name', 'id', 'gender', 'birth_date']


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'id', 'birth_date']


class AddressAdmin(admin.ModelAdmin):
	list_display = ['street', 'id', 'zip_code', 'city']


class DoctorAdmin(admin.ModelAdmin):
	list_display = ['surname', 'id', 'name']
	inlines = [OpeningHoursInline]


class OpeningHoursAdmin(admin.ModelAdmin):
	list_display = ['from_hour', 'to_hour', 'day', 'id']


admin.site.register(CatProfile, CatProfileAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(OpeningHours, OpeningHoursAdmin)