from django.views.generic.base import TemplateView
from django.http import Http404
from django.shortcuts import redirect

from bayesian_networks.models import Challenge, BayesianNetwork


class IndexView(TemplateView):
    """ View returning the homepage of the app """
    template_name = 'bayesian_networks/index.html'

    def get_context_data(self, **kwargs):
        """ Returns list containing all challenges """
        context = super().get_context_data(**kwargs)
        context['challenges'] = Challenge.objects.all().order_by('name').values()
        return context


class BayesianNetworkView(TemplateView):
    """ View containing a single Bayesian Network to be solved """
    template_name = 'bayesian_networks/network.html'
    challenge = None
    network = None
    is_final_network = None

    def dispatch(self, request, *args, **kwargs):
        # Find the requested challenge
        self.challenge = Challenge.objects.filter(id=kwargs['id'])
        if not self.challenge.count():
            raise Http404

        # Find the requested Bayesian network of the challenge
        self.challenge = self.challenge.first()
        self.network = BayesianNetwork.objects.filter(challenge=self.challenge, position=kwargs['position'])
        if not self.network.count():
            # Redirect to homepage if a challenge has no networks
            if kwargs['position'] == 1:
                return redirect('no-networks')

            raise Http404

        self.is_final_network = BayesianNetwork.objects.filter(challenge=self.challenge).count() == kwargs['position']
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['challenge_name'] = self.challenge.name
        context['challenge_id'] = kwargs['id']
        context['previous_position'] = kwargs['position'] - 1
        context['next_position'] = kwargs['position'] + 1
        context['network'] = self.network.first().network
        context['is_final_network'] = self.is_final_network
        return context


class NoNetworksView(TemplateView):
    """ Redirect view for challenges having no networks """
    template_name = 'bayesian_networks/no_networks.html'
