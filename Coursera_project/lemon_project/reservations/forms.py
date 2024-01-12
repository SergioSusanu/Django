from . import models
from django.forms import ModelForm


class ReservationForm(ModelForm):
    class Meta:
        model = models.Reservations
        fields = '__all__'

