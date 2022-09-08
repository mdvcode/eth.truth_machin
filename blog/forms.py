from django import forms

from blog.models import Transaction


class CreateTextTransForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('to_account', 'gas', 'data', 'gas_price',)


class UpdateTextTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('to_account', 'gas', 'data', 'gas_price',)






