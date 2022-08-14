from dataclasses import field
from pyexpat import model
from .models import goodesModel
from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from .validator import validate_select_option
class NewGoodes(ModelForm):
    class Meta:
        model = goodesModel
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(NewGoodes, self).__init__(*args, **kwargs)
        self.fields['Title'].label = ""
        self.fields['Title'].widget.attrs['placeholder'] = "Назва"
        
        self.fields['version'].label = ""
        self.fields['version'].widget.attrs['placeholder'] = "Версія"
        
        self.fields['article'].label = ""
        self.fields['article'].widget.attrs['placeholder'] = "Артикль"
        
        self.fields['material'].label = ""
        self.fields['material'].widget.attrs['placeholder'] = "Матеріал"
        
        self.fields['furniture'].label = ""
        self.fields['furniture'].widget.attrs['placeholder'] = "Фурнітура"
        
        self.fields['colors'].label = ""
        self.fields['colors'].widget.attrs['placeholder'] = "Колір"
        
        self.fields['price'].label = ""
        self.fields['price'].widget.attrs['placeholder'] = "Ціна"
        
        self.fields['imageGoodes'].label = ""
        self.fields['imageGoodes'].widget.attrs['placeholder'] = "Фото"

logo_choise = [
    ('', 'Нанесення логотипу'),
    ('Ні', 'Ні'),
    ('Так', 'Так'),
]
Design_choise = [
    ('', 'Наявність макету/дизайну'),
    ('Ні', 'Ні'),
    ('Так', 'Так'),
]
class ordersForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': "ordersForm__name"}), max_length=255)
    goods = forms.CharField(widget=forms.TextInput(attrs={'class': "ordersForm__goods"}), max_length=255)
    material = forms.CharField(widget=forms.TextInput(attrs={'class': "ordersForm__material"}), required=False, max_length=255)
    count = forms.CharField(widget=forms.TextInput(attrs={'class': "ordersForm__count"}))
    brand = forms.CharField(widget=forms.Select(attrs={'class': "ordersForm__brand"}, choices=logo_choise), validators=[validate_select_option])
    maket = forms.CharField(widget=forms.Select(attrs={'class': "ordersForm__maket"}, choices=Design_choise), validators=[validate_select_option])
    time = forms.CharField(max_length=255)
    number = forms.CharField(widget=forms.TextInput(), max_length=12)
    message = forms.CharField(widget=forms.Textarea(),required=False)

    def __init__(self, *args, **kwargs):
        super(ordersForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['name'].widget.attrs['placeholder'] = "ПІБ"
        
        self.fields['goods'].label = ""
        self.fields['goods'].widget.attrs['placeholder'] = "Найменування товарів"
        
        self.fields['material'].label = ""
        self.fields['material'].widget.attrs['placeholder'] = "* Матеріал"

        self.fields['brand'].label = ""
        self.fields['maket'].label = ""
        
        self.fields['count'].label = ""
        self.fields['count'].widget.attrs['placeholder'] = "Кількість (шт.)"

        self.fields['time'].label = ""
        self.fields['time'].widget.attrs['placeholder'] = "Приблизний термін"
        
        self.fields['number'].label = ""
        self.fields['number'].widget.attrs['placeholder'] = "Номер телефону"
        self.fields['number'].widget.attrs['value'] = "38"

        self.fields['message'].label = ""
        self.fields['message'].widget.attrs['placeholder'] = "* Ваші побажання"

class RepluuGoodesinfo(ModelForm):
    class Meta:
        model = goodesModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(RepluuGoodesinfo, self).__init__(*args, **kwargs)
        self.fields['Title'].label = ""
        self.fields['Title'].widget.attrs['placeholder'] = "Назва"
        
        self.fields['version'].label = ""
        self.fields['version'].widget.attrs['placeholder'] = "Версія"
        
        self.fields['article'].label = ""
        self.fields['article'].widget.attrs['placeholder'] = "Артикль"
        
        self.fields['material'].label = ""
        self.fields['material'].widget.attrs['placeholder'] = "Матеріал"
        
        self.fields['furniture'].label = ""
        self.fields['furniture'].widget.attrs['placeholder'] = "Фурнітура"
        
        self.fields['colors'].label = ""
        self.fields['colors'].widget.attrs['placeholder'] = "Колір"
        
        self.fields['price'].label = ""
        self.fields['price'].widget.attrs['placeholder'] = "Ціна"
        
        self.fields['imageGoodes'].label = ""
        self.fields['imageGoodes'].widget.attrs['placeholder'] = "Фото"




