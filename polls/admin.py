from django.contrib import admin

from .models import Booking, Campaign

admin.site.register([Campaign, Booking])
