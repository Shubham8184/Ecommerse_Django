from django.urls import path
from .views import CustomerAddressUpdateView,CustomerAddressview, Customeraddressdeleteview, Customeralladdressview, load_states,load_cities



urlpatterns=[
    path('customeradddelete/<int:delete>',Customeraddressdeleteview,name='customeraddressdelete'),
    # path('customeraddupdate/<int:update>',CustomerAddressupdateview,name='customeraddressupdate'),
    path('customeralladd/',Customeralladdressview,name='customeralladdress'),
    path('customeradd/',CustomerAddressview,name='customeraddress'),
    path('ajax/load-states/', load_states, name='ajax_load_states'),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
    path('customeraddupdate/<int:pk>',CustomerAddressUpdateView.as_view(),name='customeraddressupdate'),

]


