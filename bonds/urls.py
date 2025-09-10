from django.urls import path
from .views import HomeView, CreateBondView, BondListView

app_name = 'bonds'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateBondView.as_view(), name='create'),
    path('list/', BondListView.as_view(), name='bond_list'),
]