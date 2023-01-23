from django import forms


class CreateBookingForm(forms.Form):
    booking_id = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Booking Id",
        error_messages={
            "required": "This field required number",
            "invalid": "This field can only type number",
        },
    )
    location_id = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Location Id",
        error_messages={
            "required": "This field required number",
            "invalid": "This field can only type number",
        },
    )
    creative_id = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Creative Id",
        error_messages={
            "required": "This field required number",
            "invalid": "This field can only type number",
        },
    )
    start_date = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={"type": "datetime-local", "class": "form-control"}
        ),
        label="Start Date",
    )
    end_date = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={"type": "datetime-local", "class": "form-control"}
        ),
        label="End Date",
    )

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if start_date and end_date and start_date > end_date:
            print("start date after end date")
            raise forms.ValidationError(
                {"start_date": "Start date must be before End date"}
            )
