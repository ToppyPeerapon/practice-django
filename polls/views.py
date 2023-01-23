import json

from django import forms
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.views.generic.edit import FormView

from .forms import CreateBookingForm
from .model_form import CreativeForm
from .models import Booking, Campaign, Creative, Location


class Success(View):
    def get(self,request):
        return HttpResponse('Success')

class index(View):
    def get(self, request):
        booking_data = Booking.objects.all().values()
        template = loader.get_template("booking/index.html")
        context = {"booking": booking_data}
        return HttpResponse(template.render(context, request))


class CreativeView(CreateView):
    model = Creative
    form_class = CreativeForm
    template_name = "creative/index.html"
    success_url = reverse_lazy('advertisement:success')

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class CreateBooking(View):
    def post(self, request):
        form = CreateBookingForm(request.POST)
        if form.is_valid():
            response = Booking.objects.create(
                booking_id=request.POST["booking_id"],
                location_id=request.POST["location_id"],
                creative_id=request.POST["creative_id"],
                start_date=request.POST["start_date"],
                end_date=request.POST["end_date"],
            )
            return HttpResponseRedirect(
                reverse("advertisement:booking_id", args=[response.id])
            )
        else:
            context = {"form": form}
            return render(request, "booking/create_form.html", context)
        #     return HttpResponse(form.errors.as_json(), headers={
        #         'Content-Type': 'application/json',
        #         'status-code': '400',
        #     })
        # print(form.errors)
        # return render(request, 'booking/create_form.html', { 'form': form })

    def get(self, request, *args, **kwargs):
        form = CreateBookingForm()
        return render(request, "booking/create_form.html", {"form": form})


class Login(View):
    def get(self, request):
        return render(request, "login/login.html")


class DetailBooking(View):
    def get(self, request, *args, **kwargs):
        booking_id = self.kwargs.get("booking_id")
        try:
            data = Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            raise Http404("This booking id does not exist")
        return render(request, "booking/detail.html", {"data": data})


# class CreateBooking(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'booking/create.html')
#
#     def post(self, request):
#         booking_id = request.POST['booking_id']
#         print(booking_id, type(booking_id))
#         response = Booking.objects.create(booking_id=request.POST['booking_id'],
#                                           location_id=request.POST['location_id'],
#                                           creative_id=request.POST['creative_id'],
#                                           start_date=request.POST['start_date'],
#                                           end_date=request.POST['end_date'],
#                                           )
#         return HttpResponseRedirect(reverse('advertisement:booking_id', args=[response.id]))


@method_decorator(csrf_exempt, name="dispatch")
class CampaignAPI(View):
    def get(self, request, *args, **kwargs):
        data = Campaign.objects.all().values()
        response_data = list(data)
        return JsonResponse(response_data, safe=False)

    def post(self, request, *args, **kwargs):
        request_data = json.loads(request.body)

        title = request_data.get("title")
        if title is None:
            return HttpResponse(
                "Can't get title from request",
                headers={
                    "Content-Type": "application/json",
                    "status-code": "400",
                },
            )
        data = Campaign.objects.create(title=title)
        return HttpResponse(
            data,
            headers={
                "Content-Type": "application/json",
                "status-code": "201",
            },
        )


@method_decorator(csrf_exempt, name="dispatch")
class CreativeAPI(View):
    def get(self, request, *args, **kwargs):
        data = Creative.objects.all().values()
        response_data = list(data)
        return JsonResponse(response_data, safe=False)

    def post(self, request, *args, **kwargs):
        request_data = json.loads(request.body)

        name = request_data.get("name")
        if name is None:
            return HttpResponse(
                "Can't get name from request",
                headers={
                    "Content-Type": "application/json",
                    "status-code": "400",
                },
            )
        data = Creative.objects.create(name=name)
        return HttpResponse(
            data,
            headers={
                "Content-Type": "application/json",
                "status-code": "201",
            },
        )


@method_decorator(csrf_exempt, name="dispatch")
class LocationAPI(View):
    def get(self, request, *args, **kwargs):
        data = Location.objects.all().values()
        response_data = list(data)
        return JsonResponse(response_data, safe=False)

    def post(self, request, *args, **kwargs):
        request_data = json.loads(request.body)

        panel_id = request_data.get("panel_id")
        if panel_id is None:
            return HttpResponse(
                "Can't get name from request",
                headers={
                    "Content-Type": "application/json",
                    "status-code": "400",
                },
            )
        data = Location.objects.create(panel_id=panel_id)
        return HttpResponse(
            data,
            headers={
                "Content-Type": "application/json",
                "status-code": "201",
            },
        )


@method_decorator(csrf_exempt, name="dispatch")
class BookingAPI(View):
    def get(self, request, *args, **kwargs):
        data = Booking.objects.all().values()
        response_data = list(data)
        return JsonResponse(
            response_data,
            safe=False,
            headers={
                "status-code": "200",
                "Access-Control-Allow-Origin": "http://localhost:3000",
                "Access-Control-Allow-Methods": "POST",
            },
        )

    def post(self, request, *args, **kwargs):
        request_data = json.loads(request.body)
        response_data = Booking.objects.create(
            booking_id=request_data.get("booking_id"),
            start_date=request_data.get("start_date"),
            end_date=request_data.get("end_date"),
            creative_id=request_data.get("creative_id"),
            location_id=request_data.get("location_id"),
        )
        return HttpResponse(
            "create success",
            headers={
                "Content-type": "application/json",
                "status-code": "201",
                "Access-Control-Allow-Origin": "http://localhost:3000",
            },
        )
