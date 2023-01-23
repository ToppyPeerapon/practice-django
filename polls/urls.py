from django.urls import path

from . import views

app_name = "advertisement"
urlpatterns = [
    path("booking/", views.index.as_view(), name="index"),
    path("<int:booking_id>/", views.DetailBooking.as_view(), name="booking_id"),
    path("create_booking/", views.CreateBooking.as_view(), name="create_booking"),
    path("creative/", views.CreativeView.as_view(), name="creative"),
    path("success/", views.Success.as_view(), name='success')
    # path("create_booking_form/", views.CreateBookingForm.as_view(), name='create_booking_form')
]
