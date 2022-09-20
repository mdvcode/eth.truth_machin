from django import forms

from blog.models import Transaction, MetamaskAccount


class CreateTextTransForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('data',)


class UpdateTextTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('data',)


class ConnectWallet(forms.ModelForm):
    class Meta:
        model = MetamaskAccount
        fields = ('user_wallet_address',)






