from rest_framework import serializers
from .models import Bank, Branch
from rest_framework import generics

class BankSerializer (serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ('name',)

class BranchSerializer (serializers.ModelSerializer):
    bank = serializers.SerializerMethodField('get_bank_name')
    class Meta:
        model = Branch
        fields=('ifsc','bank','branch','address','city','district','state')

    def get_bank_name (self, obj):
        return obj.bank_id.name
