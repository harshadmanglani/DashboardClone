from django.forms import ModelForm
from .models import *
from django.utils.translation import gettext_lazy as _

class ClaimForm(ModelForm):
    class Meta:
        model = InsuranceClaim
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClaimForm, self).__init__(*args, **kwargs)
        self.fields['inspector_comments'].required = False