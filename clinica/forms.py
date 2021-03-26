from django import forms
from django.forms import ModelForm


default_errors = {
    'required': 'Esse campo precisa ser preenchido',
    'invalid': 'Valor inválido',
}

class VaccineRegister(forms.Form):

    short_description_field = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Descrição ou nome da vacina*', 'style': 'height: 30px; font-size: 13px;'}), error_messages=default_errors)
    long_description_field = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Comentários', 'style': 'font-size: 13px;'}), error_messages=default_errors)
    quantity_field = forms.DecimalField(label="Quantidade", widget=forms.NumberInput(attrs={'style': 'height: 30px; font-size: 13px;'}), error_messages=default_errors)
    unit_price_field = forms.DecimalField(label="Preço Unitário (R$)", widget=forms.NumberInput(attrs={'style': 'height: 30px; font-size: 13px;'}), error_messages=default_errors)

    def __init__(self, *args, **kwargs):
        super(VaccineRegister, self).__init__(*args, **kwargs)
        self.fields['short_description_field'].label = False
        self.fields['long_description_field'].label = False


class VaccineBrowse(forms.Form):

    filter_short_description_field = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Filtrar por descrição', 'style': 'height: 30px; font-size: 13px;'}))
    filter_long_description_field = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Filtrar por comentário', 'style': 'font-size: 13px;'}))
    filter_min_quantity_field = forms.DecimalField(required=False, label="Quantidade mínima", widget=forms.NumberInput(attrs={'style': 'height: 30px; font-size: 13px;'}))
    filter_max_quantity_field = forms.DecimalField(required=False, label="Quantidade máxima", widget=forms.NumberInput(attrs={'style': 'height: 30px; font-size: 13px;'}))
    filter_min_unit_price_field = forms.DecimalField(required=False, label="Preço Unitário minímo (R$)", widget=forms.NumberInput(attrs={'style': 'height: 30px; font-size: 13px;'}))
    filter_max_unit_price_field = forms.DecimalField(required=False, label="Preço Unitário máximo (R$)", widget=forms.NumberInput(attrs={'style': 'height: 30px; font-size: 13px;'}))

    def __init__(self, *args, **kwargs):
        super(VaccineBrowse, self).__init__(*args, **kwargs)
        self.fields['filter_short_description_field'].label = False
        self.fields['filter_long_description_field'].label = False
