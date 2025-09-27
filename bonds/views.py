from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from bonds.models import Bond, BondPrice
from .forms import BondForm, BondPriceForm
from .calculations import create_fixed_bond


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
    form_class = BondForm
    template_name = 'bonds/bond_update.html'
    success_url = '/bonds/'

class DeleteBondView(DeleteView):
    model = Bond
    success_url = '/bonds/'

class BondListView(ListView):
    model = Bond
    template_name = 'bonds/list_bonds.html'
    context_object_name = 'bonds'

    def get_queryset(self):
        return Bond.objects.filter(is_active=True)

class BondDetailView(DetailView):
    """
    View for displaying bond details.

    The BondDetailView class is designed to display the details of a specific
    bond by inheriting from Django's built-in DetailView. This view
    fetches the bond data and calculates additional related details
    to display as part of the context.

    :ivar model: The model associated with this view, which is Bond.
    :type model: type
    :ivar context_object_name: The key used in the context to refer to the object,
        which is 'bond' in this case.
    :type context_object_name: str
    :ivar template_name: The path to the template used for rendering the bond details view.
    :type template_name: str
    """
    model = Bond
    context_object_name = 'bond'
    template_name = 'bonds/detail_bond.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        the_bond = Bond.objects.get(pk=3)
        bond_calculations = create_fixed_bond(the_bond)
        context['ql_bond'] = bond_calculations
        return context

    def get_queryset(self):
        return Bond.objects.filter(is_active=True, pk=self.kwargs.get('pk'))

class AddBondPriceView(CreateView):
    model = BondPrice
    form_class = BondPriceForm
    template_name = 'bonds/add_bond_price.html'

    def get_success_url(self):
        return reverse_lazy('bonds:list_bond_prices', kwargs={'pk': self.object.bond.pk})


class BondPriceListView(ListView):
    """
    Represents a list view specifically for displaying bond prices.

    This class provides functionality to display a list of bond prices
    associated with a specific bond. It customizes the queryset and allows
    the use of a specific template and context variable name.

    :ivar model: The model that the view will be interacting with, which is
        BondPrice.
    :type model: Model
    :ivar context_object_name: The name of the context object used for
        rendering in the template, set to "bond_prices".
    :type context_object_name: str
    :ivar template_name: The name of the template used for rendering the
        list view.
    :type template_name: str
    """
    model = BondPrice
    context_object_name = 'bond_prices'
    template_name = 'bonds/list_bond_prices.html'

    def get_context_data(self, *args, **kwargs):
        """
        Get the context data for the view.

        This method retrieves context data used in templates by invoking the parent class's
        get_context_data method and optionally modifies or extends the context.

        :param args: Positional arguments passed to the method.
        :type args: tuple
        :param kwargs: Keyword arguments passed to the method.
        :type kwargs: dict
        :return: Context data dictionary that can be used by the view.
        :rtype: dict
        """
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """
        Filters and retrieves a queryset of BondPrice objects based on the bond ID
        provided in the URL parameters.

        :param self: The instance of the current view or object calling this method.
        :return: A queryset of BondPrice objects filtered by the provided bond ID.
        :rtype: QuerySet
        """
        bond_pk = self.kwargs.get('pk')
        return BondPrice.objects.filter(bond_id=bond_pk)
