from django.db import models


class IndexInfo(models.Model):
    objects = None
    phone = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)
    instagram = models.CharField(max_length=250)


class AccountMetamask(models.Model):
    objects = None
    active = models.BooleanField(default=True)
    user_wallet_address = models.CharField(max_length=255)
    balance = models.FloatField(default=0)
    count_trans = models.IntegerField(default=0)

    def __str__(self):
        return self.user_wallet_address


class Transaction(models.Model):
    objects = None
    account = models.ForeignKey(AccountMetamask, null=True, blank=True, on_delete=models.CASCADE)
    to_account = models.CharField(max_length=250, null=True, blank=True)
    gas = models.IntegerField(default=0)
    value = models.FloatField(default=0)
    gas_price = models.IntegerField(default=0)
    res_hash = models.CharField(max_length=250, null=True, blank=True)
    data = models.CharField(max_length=5000, null=True, blank=True)
    text = models.CharField(max_length=250, null=True, blank=True)



