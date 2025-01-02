from django import forms
from .models import Category, Material


class ProductForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.friendly_name) for c in categories]

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'




