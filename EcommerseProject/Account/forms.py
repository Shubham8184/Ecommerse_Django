from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Customer, Seller


class CustomerCreationForm(UserCreationForm):
    name=forms.CharField(max_length=50)
    class Meta:
        model = CustomUser
        fields = ('name','mobile_no','email')

        labels={
            'name':'Customer Name',
            'mobile_no':'Mobile No.',
            'email':'Email Address'
        }

        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter Your valid mobile no.'}),
            'mobile_no':forms.TextInput(attrs={'placeholder':'Enter Your valid mobile no.'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter Your valid email address'}),
        }

    
    # def clean(self):
    #     all_data=super().clean()
    #     mobile=all_data.get('mobile_no')
    #     if mobile<9 or mobile>11:
    #         raise forms.ValidationError('Mobile No. must be 10 number.')

    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.is_active=False
        user.save()
        nm=self.cleaned_data.get('name')
        customer = Customer.objects.create(user=user,name=nm)
        return user

class SellerCreationForm(UserCreationForm):
    company_name=forms.CharField(max_length=50)
    gst_no=forms.CharField(max_length=200)
    bank_account=forms.IntegerField()
    address=forms.CharField(max_length=1000)
    class Meta:
        model = CustomUser
        fields = ('company_name','mobile_no','email')
        labels={
            'company_name':'Company Name',
            'mobile_no':'Contact No.',
            'email':'Email Address',
            'gst_no':'GST No.',
            'bank_account':'Bank Account No.'
        }
        widgets={
            'company_name':forms.TextInput(attrs={'placeholder':'Enter your company name'}),
            'mobile_no':forms.TextInput(attrs={'placeholder':'Enter your mobile number'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter your email address'}),
            'gst_no':forms.TextInput(attrs={'placeholder':'Enter your company GST no.'}),
            'bank_account':forms.TextInput(attrs={'placeholder':'Enter your company Bank Account'}),
            'address':forms.Textarea(attrs={'placeholder':'Enter your company address here....'}),
            
            
        }
    
    # def clean(self):
    #     all_data=super().clean()
    #     mobile=all_data.get('mobile_no')
    #     gst=all_data.get('gst_no')
    #     bank=all_data.get('bank_account')
    #     if mobile<10 or mobile>10:
    #         raise forms.ValidationError('Mobile No. must be 10 number.')
    #     if gst<15 or gst>15:
    #         raise forms.ValidationError('GST No. must be 15 charactors.')
    #     if bank<11 or bank>11:
    #         raise forms.ValidationError('Bank Account No. must be 11 numbars.')
        

        

    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.is_active=False
        user.save()
        a=self.cleaned_data.get('address')
        b=self.cleaned_data.get('bank_account')
        c=self.cleaned_data.get('company_name')
        g=self.cleaned_data.get('gst_no')
        customer = Seller.objects.create(user=user,company_name=c,gst_no=g,address=a,bank_account=b)
        return user




