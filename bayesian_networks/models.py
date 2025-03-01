from django.db import models


class Challenge(models.Model):
    """ Challenge consisting of many Bayesian networks to be solved by the user """
    name = models.CharField(max_length=100, null=False, default='Challenge')

    def __str__(self):
        return self.name


class BayesianNetwork(models.Model):
    """ Solvable Bayesian network """
    network = models.CharField(max_length=255, verbose_name='Bayesian network')
    position = models.PositiveSmallIntegerField(default=1)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='bayesian_networks')
