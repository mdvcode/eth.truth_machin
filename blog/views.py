import binascii

from django.contrib.sites.models import Site
from django.shortcuts import render, redirect
from web3 import Web3, HTTPProvider

from .forms import CreateTextTransForm, UpdateTextTransactionForm, ConnectWallet
from .models import IndexInfo, Transaction, MetamaskAccount


def home(request):
    index = IndexInfo.objects.all()[0]
    current_site = Site.objects.get_current()
    w3 = Web3(HTTPProvider())
    return render(request, 'blog/content.html', context={'domain': current_site.domain,
                                                         'index': index, 'w3': w3})


def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(' ', '').replace('0x', '').replace('\t', '').replace('\n', '')
    ascii_str = binascii.unhexlify(hex_str.encode())
    return ascii_str


def create_text_trans(request):
    index = IndexInfo.objects.all()[0]
    if request.method == "POST":
        form = ConnectWallet(data=request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.save()
    form = ConnectWallet()
    # form = CreateTextTransForm
    # transactions = Transaction.objects.filter()
    # if request.method == 'POST':
    #     form = CreateTextTransForm(request.POST)
    #     if form.is_valid():
    #         inst = form.save(commit=False)
    #         inst.account = MetamaskAccount.objects.filter()
    #         inst.save()
            # w3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/27709d11030e4a8f8a3066732c9e6b90"))
            # construct_txn = {
            #     'from': w3.toChecksumAddress(account.user_wallet_address),
            #     'nonce': w3.eth.getTransactionCount(w3.toChecksumAddress(account.user_wallet_address)),
            #     'to': w3.toChecksumAddress(inst.to_account),
            #     'gas': inst.gas,
            #     'data': inst.data.encode('utf-8'),
            #     'gasPrice': w3.toWei(inst.gas_price, 'gwei')}
            # signed_tx = w3.eth.account.signTransaction(construct_txn, inst.account.private_key)
            # tx_hash = w3.eth.sendRawTransaction(Web3.toHex(signed_tx.rawTransaction))
            # Transaction.objects.filter(id=inst.id).update(res_hash=str(tx_hash.hex()))
            # transaction = w3.eth.getTransaction(tx_hash)
            # Transaction.objects.filter(id=inst.id).update(data=transaction.get('input'))
            # Transaction.objects.filter(id=inst.id).update(text=hex_to_ascii(transaction.get('input')).decode('utf-8'))
            # return redirect('blog:update_texttrans', id_transaction=inst.id)
        # form = CreateTextTransForm()
    return render(request, 'blog/create_text_trans.html', context={'form': form,
                                                                   'index': index})


def update_texttrans(request, id_transaction):
    index = IndexInfo.objects.all()[0]
    transactions = Transaction.objects.get(id=id_transaction)
    if request.method == 'POST':
        form = UpdateTextTransactionForm(instance=transactions, data=request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('blog:update_texttrans', id_transaction=id_transaction)
    form = UpdateTextTransactionForm(instance=transactions)
    s = transactions.data.encode('utf-8')
    data = str(s.hex())
    return render(request, 'blog/update_texttrans.html', context={'form': form, 'data': data, 'index': index})
