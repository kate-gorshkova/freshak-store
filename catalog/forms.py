from logging import PlaceHolder
from .models import Goods
from django.forms import ModelForm, TextInput, Textarea, NumberInput, DateInput


class DateInputWidget(DateInput):
    input_type = 'date'

    def format_value(self, value):
        return value


class GoodsForm(ModelForm):
    class Meta:
        model = Goods
        fields = ['title', 'description', 'price', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Название товара'
            }),
            'description': Textarea(attrs={
                'class':'form-control',
                'placeholder':'Описание товара'
            }),
            'price': NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Цена товара в рублях',
                'min': '0',
            }),
            'date': DateInputWidget(attrs={
                'class':'form-control',
                'placeholder':'Дата поставки'
            })
        }
