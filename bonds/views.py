from django.views.generic import TemplateView, ListView, DetailView


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

class AboutView(TemplateView):
    template_name = 'bonds/about.html'
    extra_context = {
        'title': 'About'}

    def get_queryset(self):
        return

class ListingView(ListView):
    template_name = 'bonds/listing.html'
    extra_context = {
        'title': 'Listing'}

class DetailView(DetailView, pk_url_kwarg='id'):
    template_name = 'bonds/detail.html'
    extra_context = {
        'title': 'Detail'}

    def get_queryset(self, pk_url_kwarg):
        return Bond.objects.filter(id=pk_url_kwarg)