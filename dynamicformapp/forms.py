# from django import forms
# from .models import DynamicFormData

# dynamicformapp/forms.py
from django import forms
from .models import DynamicFormData

class DynamicFormDataForm(forms.ModelForm):
    class Meta:
        model = DynamicFormData
        fields = ['name', 'password', 'data']

DynamicFormDataFormSet = forms.modelformset_factory(DynamicFormData, form=DynamicFormDataForm, extra=1)



