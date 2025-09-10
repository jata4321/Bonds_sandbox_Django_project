from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from bonds.models import Bond, BondPrice


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
    fields = [
        'name',
        'ISIN',
        'issue_date',
        'maturity_date',
        'coupon_rate',
        'coupon_frequency',
        'quantity',
        'issue_price',
        'is_active',
    ]
    template_name = 'bonds/create_bond.html'
    success_url = '/bonds/'


class UpdateBondView(UpdateView):
    model = Bond

class BondListView(ListView):
    model = Bond
    object_name = 'bonds'

    def get_queryset(self, active=True):
        return Bond.objects.filter(is_active=active)

class BondDetailView(DetailView):
    model = Bond
    object_name = 'bond'

    def get_queryset(self, active=True):
        return Bond.objects.filter(is_active=active)

class BondPriceCreateView(CreateView):
    model = BondPrice
    fields = ['name', 'price', 'date']