from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    """
    Home page

    **Template**
    :template:`core/index.html`
    """
    template_name = '../templates/core/index.html'
