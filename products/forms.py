from django import forms
from products.models import Product



class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['number_of_views']

    def __init__(self,*args,**kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)
        for visible_field in self.visible_fields():
            if visible_field.field.label != "Product image":
                visible_field.field.widget.attrs['class'] = "form-control"
