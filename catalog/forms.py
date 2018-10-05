from django.forms import ModelForm
from .models import Book
from django import forms
from suit.widgets import SuitDateWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BookForm(ModelForm):
    publish_date = forms.DateField(widget=SuitDateWidget)

    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save book'))