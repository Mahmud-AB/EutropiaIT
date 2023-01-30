from django.forms import ModelForm
from .models import News

class newsform(ModelForm):
    class Meta:
        model=News
        fields=['cover_img','title','n_details']