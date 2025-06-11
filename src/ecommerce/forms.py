from django  import forms 
from .models import ProductModel
class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = [
            "title",
            "price",
            "description",
            "seller",
            "color",
            "Product_dimensions" 
        ]