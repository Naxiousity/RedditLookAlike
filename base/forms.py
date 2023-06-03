from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' #It means that whatever is under the model "Room", it will automatically make a form based on whats written there e.g. host, topic, name, desc etc.
        