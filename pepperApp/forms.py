from django import forms

from .models import db


class db_form(forms.ModelForm):
    class Meta:
        model = db
        fields = ['username', 'email']

    ################################
    # Example of Custom Validation #
    ################################
    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     print username
    #     if "*" in username:
    #         raise forms.ValidationError("Please do not use * in username")
    #     return username