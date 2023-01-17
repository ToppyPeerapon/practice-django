from rest_framework import serializers

from .models import Booking, Campaign, Creative, Location


class CampaignSerializers(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ["id", "title"]


class CreativeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Creative
        fields = ["id", "name"]


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id",
            "booking_id",
            "start_date",
            "end_date",
            "creative_id_id",
            "location_id_id",
        ]


class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "panel_id"]
