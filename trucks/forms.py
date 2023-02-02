from django import forms
from trucks.models import Truck


class TruckForm(forms.ModelForm):

    class Meta:

        model = Truck
        fields = (
            'model',
            'number',
            'tonnage',
            'workload',
            'overload',
            )
            