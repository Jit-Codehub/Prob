from django.urls import path,include
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
path('',home, name='home'),
path('accuracy-calculator/',accuracy_calculator, name= 'accuracy'),
path('bayes-theorem-calculator/',bayes_theorem_calculator, name= 'bayes-theorem'),
path('binomial-probability-calculator/',binomial_probability_calculator, name= 'binomial-probability-calculator'),
path('binomial-probability-distribution-calculator/',binomial_probability_distribution_calculator, name= 'binomial_distribution'),
path('birthday-paradox-calculator/',birthday_paradox_calculator, name= 'birthday-paradox'),
path('chebyshevs-theorem-calculator/',chebyshevs_theorem_calculator, name= 'cheb-theorem'),
path('chi-square-probability-calculator/',chi_square_probability_calculator, name= 'chi_square'),
path('coin-flip-probability-calculator/',coin_flip_probability_calculator, name= 'coin_flip_probability'),
path('coin-toss-probability-calculator/',coin_toss_probability_calculator, name= 'coin-toss-probability-calculator'),
path('combinations-calculator/',combinations_calculator, name= 'combinations'),
path('cumulative-probability-calculator/',cumulative_probability_calculator, name= 'cumulative'),
path('deck-of-cards-probability-calculator/',deck_of_cards_probability_calculator, name= 'deck-of-cards-probability-calculator'),
path('dependent-probability-calculator/',dependent_probability_calculator, name= 'dependent-probability-calculator'),
path('dice-probability-calculator/',dice_probability_calculator, name= 'dice-probability-calculator'),
path('dice-roll-probability-calculator/',dice_roll_probability_calculator, name= 'dice-roll-probability-calculator'),
path('discrete-probability-distribution-calculator/',discrete_probability_distribution_calculator, name= 'discrete-probability-distribution-calculator'),
path('empirical-probability-calculator/',empirical_probability_calculator, name= 'empirical-probability-calculator'),
path('expected-value-calculator/',expected_value_calculator, name= 'expected_value_calculator'),
path('experimental-probability-calculator/',experimental_probability_calculator, name= 'experimental-probability-calculator'),
path('exponential-probability-calculator/',exponential_probability_calculator, name= 'exponential-probability-calculator'),
path('geometric-probability-calculator/',geometric_probability_calculator, name= 'geometric-probability-calculator'),
path('independent-probability-calculator/',independent_probability_calculator, name= 'independent-probability-calculator'),
path('labor-probability-calculator/',labor_probability_calculator, name= 'labor-probability-calculator'),
path('life-expectancy-probability-calculator/',life_expectancy_probability_calculator, name= 'life-expectancy-probability-calculator'),
path('lottery-probability-calculator/',lottery_probability_calculator, name= 'lottery-probability-calculator'),
path('mean-of-probability-distribution-calculator/',mean_of_probability_distribution_calculator, name= 'mean-of-probability-distribution-calculator'),
path('odds-calculator/',odds_calculator, name= 'odds-calculator'),
path('options-probability-calculator/',options_probability_calculator, name= 'options-probability-calculator'),
path('percentage-probability-calculator/',percentage_probability_calculator, name= 'percentage-probability-calculator'),
path('permutations/',permutations, name= 'permutations'),
path('poisson-probability-calculator/',poisson_probability_calculator, name= 'poisson-probability-calculator'),
path('poker-probability-calculator/',poker_probability_calculator, name= 'poker-probability-calculator'),
path('probability-calculator/',probability_calculator, name= 'probability-calculator'),
path('probability-density-function-calculator/',probability_density_function_calculator, name= 'probability-density-function-calculator'),
path('probability-distribution-calculator/',probability_distribution_calculator, name= 'probability-distribution-calculator'),
path('probability-of-3-events-calculator/',probability_of_3_events_calculator, name= 'probability-of-3-events-calculator'),
path('random-number-generator/',random_number_generator, name= 'random-number-generator'),
path('relative-risk-calculator/',relative_risk_calculator, name= 'relative-risk-calculator'),
path('risk-calculator/',risk_calculator, name= 'risk-calculator'),
path('roulette-probability-calculator/',roulette_probability_calculator, name= 'roulette-probability-calculator'),
path('sensitivity-and-specificity-calculator/',sensitivity_and_specificity_calculator, name= 'sensitivity-and-specificity-calculator'),
path('standard-deviation-probability-calculator/',standard_deviation_probability_calculator, name= 'standard-deviation-probability-calculator'),
path('uniform-probability-distribution-calculator/',uniform_probability_distribution_calculator, name= 'uniform-probability-distribution-calculator'),
path('variance-probability-calculator/',variance_calculator_probability, name= 'variance-probability-calculator'),
path('yugioh-probability-calculator/',yugioh_probability_calculator, name= 'yugioh-probability-calculator'),
path('z-score-probability-calculator/',z_score_probability_calculator, name= 'z-score-probability-calculator'),
path('bag-of-marble-pobability-calculator/',marbleprob, name= 'bag-of-marble-probability'),

path('privacy-policy/',privacy_policy, name='privacy-policy'),
path('disclaimer/',disclaimer, name='privacy-policy')


    
]
urlpatterns+=staticfiles_urlpatterns()