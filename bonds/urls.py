from django.urls import path
from .views import (HomeView, CreateBondView,
                    BondListView, AddBondPriceView,
                    BondPriceListView, BondDetailView, UpdateBondView, DeleteBondView)

app_name = 'bonds'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateBondView.as_view(), name='create_bond'),
    path('update/<int:pk>/', UpdateBondView.as_view(), name='update_bond'),
    path('delete/<int:pk>/', DeleteBondView.as_view(), name='delete_bond'),
    path('list-bonds/', BondListView.as_view(), name='list_bonds'),
    path('detail-bond/<int:pk>/', BondDetailView.as_view(), name='detail_bond'),
    path('add-price/', AddBondPriceView.as_view(), name='add_bond_price'),
    path('list-prices/<int:pk>/', BondPriceListView.as_view(), name='list_bond_prices'),
]