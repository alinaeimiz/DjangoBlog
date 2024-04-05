from django.forms import ModelForm
from Posts.models import Newsletter,Contact

class EmailForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']