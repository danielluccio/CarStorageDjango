from django import forms
from .models import Brand, Car


class BrandForm(forms.ModelForm):
    
    class Meta:
        model = Brand
        fields = '__all__'


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

        # restricao para valores menores que 20000

    def clean_value(self):
        value = self.cleaned_data.get('value')

        if value < 20000:
            self.add_error('value', "Valor deve ser no minimo 20000")

        return value
    
    # Restricao para ano de frabricacao menores que 1975

    def clean_model_year(self):
        model_year = self.cleaned_data.get('model_year')

        if model_year < 1975:
            self.add_error('model_year', 'Ano do modelo esta abaixo do permitido !')

        else:
            return model_year
        

    # Restricao para ano de fabricacao 


    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')

        if factory_year < 1975:
            self.add_error('factory_year', 'O ano de fabricação é menor do que o esperado !')

        else:
            return factory_year