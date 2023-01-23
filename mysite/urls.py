from django.contrib import admin
from django.urls import include, path

from polls import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),
    path("login/", views.Login.as_view()),
    path("api/campaign/", views.CampaignAPI.as_view()),
    path("api/creative/", views.CreativeAPI.as_view()),
    path("api/booking/", views.BookingAPI.as_view()),
    path("api/location/", views.LocationAPI.as_view()),
]
