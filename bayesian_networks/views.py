from django.views.generic.base import TemplateView

from bayesian_networks.models import Challenge


class IndexView(TemplateView):
    """ View returning the homepage of the app """
    template_name = 'bayesian_networks/index.html'

    def get_context_data(self, **kwargs):
        """ Returns list containing all challenges """
        context = super().get_context_data(**kwargs)
        context['challenges'] = Challenge.objects.all().order_by('name').values()
        return context
