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
