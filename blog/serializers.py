from rest_framework import serializers

from blog.models import MetamaskAccount, Transaction, IPFS


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetamaskAccount
        fields = ['user_wallet_address']


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['data', 'res_hash']


class IPFSDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPFS
        fields = ['text', 'result_hash']


