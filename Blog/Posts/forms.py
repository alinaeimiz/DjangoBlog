from django.forms import ModelForm
from Posts.models import Newsletter

class EmailForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']