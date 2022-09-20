from django.db import models


class IndexInfo(models.Model):
    objects = None
    phone = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)
    instagram = models.CharField(max_length=250)


class MetamaskAccount(models.Model):
    objects = None
    user_wallet_address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user_wallet_address


class Transaction(models.Model):
    objects = None
    account = models.ForeignKey(MetamaskAccount, null=True, blank=True, on_delete=models.CASCADE)
    res_hash = models.CharField(max_length=250, null=True, blank=True)
    data = models.CharField(max_length=5000, null=True, blank=True)
    text = models.CharField(max_length=250, null=True, blank=True)


