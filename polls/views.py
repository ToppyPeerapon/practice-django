from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Booking, Campaign, Creative, Location
from .serializers import (
    BookingSerializers,
    CampaignSerializers,
    CreativeSerializers,
    LocationSerializers,
)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class CampaignAPI(APIView):
    def get(self, request):
        data = Campaign.objects.all()
        serializer = CampaignSerializers(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {"title": request.data.get("title")}
        serializer = CampaignSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreativeAPI(APIView):
    def get(self, request):
        data = Creative.objects.all()
        serializer = CreativeSerializers(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {"name": request.data.get("name")}
        serializer = CreativeSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationAPI(APIView):
    def get(self, request):
        data = Location.objects.all()
        serializer = LocationSerializers(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {"panel_id": request.data.get("panel_id")}
        serializer = LocationSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingAPI(APIView):
    def get(self, request):
        data = Booking.objects.all()
        serializer = BookingSerializers(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        creative_id = request.data.get("creative_id")
        model_creative = Creative.objects.get(id=creative_id)

        location_id = request.data.get("location_id")
        model_location = Location.objects.get(id=location_id)
        data = {
            "booking_id": request.data.get("booking_id"),
            "start_date": request.data.get("start_date"),
            "end_date": request.data.get("end_date"),
            "creative_id_id": creative_id,
            "location_id_id": location_id,
        }
        serializer = BookingSerializers(data=data)

        print("--------------------------------")
        print("model creative", model_creative)
        print("model location", model_location)
        print(request.data)
        print(data)
        print(serializer)
        print("-----------------------------")
        if serializer.is_valid():
            serializer.save()
            print("success save")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("error", serializer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
