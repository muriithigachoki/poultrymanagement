from django.forms import ModelForm
from poultry.models import Poultry
from django.contrib.auth.models import User


class PoultryForm(ModelForm):
    class Meta:
        model = Poultry
        fields = "__all__"
