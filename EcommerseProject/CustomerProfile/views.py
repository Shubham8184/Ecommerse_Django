from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from Account.models import Customer
from .models import  Address, City, Country, State
from .forms import CustomerAddressForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator




@login_required(login_url='login')
def CustomerAddressview(request):
    try:
        customer = Customer.objects.get(user=request.user)
        form = CustomerAddressForm()
        if request.method == 'POST':
            form = CustomerAddressForm(request.POST)
            print(request.POST)
            print('Before',form.is_valid())
            if form.is_valid():
                print('After',form.is_valid())
                obj = form.save(commit=False)
                obj.customer = customer
                obj.save()
                return redirect('customeralladdress')
        template_name = 'CustomerProfile/CustomerProfile.html'
        context = {'form': form}
        return render(request, template_name, context)
    except Customer.DoesNotExist:
        return redirect('logout')


# AJAX
@login_required(login_url='login')
def load_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id)
    context = {'states': states}
    return render(request, 'CustomerProfile/Statelist.html', context)


@login_required(login_url='login')
def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id)
    context = {'cities': cities}
    return render(request, 'CustomerProfile/Citylist.html', context)

@login_required(login_url='login')
def Customeralladdressview(request):
    try:
        customer = Customer.objects.get(user=request.user)
        address=Address.objects.filter(customer=customer)
        template_name='CustomerProfile/Customeralladdress.html'
        context={'address':address}
        return render(request,template_name,context)
    except Customer.DoesNotExist:
        return redirect('logout')

@login_required(login_url='login')
def Customeraddressdeleteview(request,delete):
    address=Address.objects.get(id=delete)
    address.delete()
    return redirect('customeralladdress')



# @login_required(login_url='login')
# def CustomerAddressupdateview(request,update):
#     customer = Customer.objects.get(user=request.user)
#     add=Address.objects.get(id=update)
#     form = CustomerAddressForm(instance=add)
#     print(form)
#     if request.method == 'POST':
#         form = CustomerAddressForm(request.POST,instance=add)
#         print(request.POST)
#         print('Before',form.is_valid())
#         if form.is_valid():
#             print('After',form.is_valid())
#             obj = form.save(commit=False)
#             obj.customer = customer
#             obj.save()
#             return redirect('customeralladdress')
#     template_name = 'CustomerProfile/CustomerProfile.html'
#     context = {'form': form}
#     return render(request, template_name, context)


@method_decorator(login_required, name='put')
class CustomerAddressUpdateView(UpdateView):
    model = Address
    fields = ('fname', 'lname', 'mobile','country','state','city','address','address_type')
    success_url = reverse_lazy('customeralladdress')
    template_name='CustomerProfile/CustomerProfile.html'
