from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from bonds.models import Bond, BondPrice
from .forms import BondForm, BondPriceForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'bonds/home.html'
    extra_context = {
        'title': 'Home'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_data'] = 'new_data'
        return context

    def get_queryset(self):
        return

class CreateBondView(CreateView):
    model = Bond
    form_class = BondForm
    template_name = 'bonds/create_bond.html'
    success_url = '/bonds/'


class UpdateBondView(UpdateView):
    model = Bond

class BondListView(ListView):
    model = Bond
    context_object_name = 'bonds'
    template_name = 'bonds/list_bonds.html'

    def get_queryset(self):
        return Bond.objects.filter(is_active=True)

class BondDetailView(DetailView):
    model = Bond
    object_name = 'bond'
    template_name = 'bonds/detail_bond.html'

    def get_queryset(self):
        return Bond.objects.filter(is_active=True, pk=self.kwargs.get('pk'))

class AddBondPriceView(CreateView):
    model = BondPrice
    form_class = BondPriceForm
    template_name = 'bonds/add_bond_price.html'

    def get_success_url(self):
        return reverse_lazy('bonds:list_bond_prices', kwargs={'pk': self.object.bond.pk})


class BondPriceListView(ListView):
    model = BondPrice
    context_object_name = 'bond_prices'
    template_name = 'bonds/list_bond_prices.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bond'] = Bond.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        bond_pk = self.kwargs.get('pk')
        return BondPrice.objects.filter(bond_id=bond_pk)
