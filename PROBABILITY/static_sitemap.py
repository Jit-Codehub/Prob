from django.contrib.sitemaps import Sitemap
from datetime import datetime

class Static_Sitemap(Sitemap):
    priority = 0.9
    changefreq = 'monthly'
    lastmod =datetime(2020, 9, 9)
    def items(self):
        l=['accuracy-calculator','bayes-theorem-calculator','binomial-probability-calculator',
        'binomial-probability-distribution-calculator','birthday-paradox-calculator','chebyshevs-theorem-calculator',
        'chi-square-probability-calculator','coin-flip-probability-calculator','coin-toss-probability-calculator',
        'combinations-calculator','cumulative-probability-calculator','deck-of-cards-probability-calculator',
        'dependent-probability-calculator','dice-probability-calculator','dice-roll-probability-calculator',
        'discrete-probability-distribution-calculator','empirical-probability-calculator','expected-value-calculator',
        'experimental-probability-calculator','exponential-probability-calculator','geometric-probability-calculator',
        'independent-probability-calculator','labor-probability-calculator','life-expectancy-probability-calculator',
        'lottery-probability-calculator','mean-of-probability-distribution-calculator','odds-calculator','options-probability-calculator',
        'percentage-probability-calculator','permutations','poisson-probability-calculator','poker-probability-calculator',
        'probability-calculator','probability-density-function-calculator','probability-distribution-calculator','probability-of-3-events-calculator',
        'random-number-generator','relative-risk-calculator','risk-calculator','roulette-probability-calculator','sensitivity-and-specificity-calculator',
        'standard-deviation-probability-calculator','uniform-probability-distribution-calculator','variance-probability-calculator',
        'yugioh-probability-calculator','z-score-probability-calculator','bag-of-marble-pobability-calculator','privacy-policy','disclaimer']

        return l
    def location(self, item):
        return "/"+item+"/"

