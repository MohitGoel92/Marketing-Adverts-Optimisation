# Reinforcement Learning - Thompson Sampling

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Random Selection
# After running this model numerous times, we see that the total rewards is usually between 1200 and 1300.

# Implementing Random Selection

import random
N = 10000
d = 10
ads_selected = []
sums_of_rewards = [0] * d
total_reward = 0

for n in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    total_reward = total_reward + reward

# Visualising the results

# As expected, we more or less see an even distribution of the ads selected

plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()

# We observe that advert 5 has the highest total rewards, therefore we conclude that advert 5 is the best as it 
# received the most clicks.

plt.bar(range(1,11), sums_of_rewards, color = 'green')
plt.title('Bar chart of rewards per advert')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was rewarded')
plt.show()

'''
# =============================================================================
# 
# =============================================================================

# Implementing Thompson Sampling
# Using the Thompson Sampling Algorithm, we see that the total reward is usually around 2500. Unlike the UCB 
# algorithm Thompson Sampling is probabilistic, resulting in a degree of randomness being present.
# We conclude that due to the Thompson Sampling Algorithm, we have recieved approximately double the 
# rewards as opposed to the random selection method, as a result of exploiting of the optimal advert.

N = 10000
d = 10
ads_selected = []
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d
total_reward = 0

for n in range(0, N):
    ad = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    if reward == 1:
        numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad] + 1
    else:
        numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad] + 1
    total_reward = total_reward + reward

# Visualising the results - Histogram
    
# Both charts resemble the same shape due to the more popular advert being selected more often, resulting in
# receiving more rewards.

plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show() 

plt.bar(range(1,11), numbers_of_rewards_1, color = 'grey')
plt.title('Bar chart of ads rewarded')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was rewarded')
plt.show()
'''
