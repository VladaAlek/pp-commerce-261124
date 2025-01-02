from django import forms
from .models import Category, Material


class ProductForm(forms.Model):

    class Meta:
        model = Category
        fields = '__all__'

    def __init__ (self, *args, **kwargs):
        super().__init__(args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['categpry'].choices = friendly_names
        for field_name, field in self.fields.item():
            field.widget.attrs['class'] = 'border-black rounded-0'




