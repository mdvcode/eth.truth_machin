from rest_framework import serializers

from blog.models import MetamaskAccount, Transaction


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetamaskAccount
        fields = ['user_wallet_address']


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['data']


