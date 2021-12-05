from django.contrib import admin
from .models import UserBooking


@admin.register(UserBooking)
class UserBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'status')
    search_fields = ('name', 'email', 'phone_number')
    search_fields = ['name', 'created_on', 'status']
    list_filter = ('name', 'created_on', 'status')
