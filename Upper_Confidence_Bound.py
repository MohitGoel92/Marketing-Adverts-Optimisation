# Reinforcement Learning - Upper Confidence Bound

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Random Selection
# After running the random model below numerous times, we see that the total reward is usually between 1200 and 1300.

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

# As expected, we more or less see an even distribution of the ads selected.

plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()

# We observe that advert 5 has the highest total rewards, therefore we conclude that advert 5 is the best
# as it received the most clicks.

plt.bar(range(1,11), sums_of_rewards, color = 'green')
plt.title('Bar chart of rewards per advert')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was rewarded')
plt.show()


# =============================================================================
# 
# =============================================================================

'''

# Implementing the Upper Confidence Bound
# Using the UCB algorithm, we see that the total reward is 2178 which will be the total reward every time 
# we run the algorithm as UCB is deterministic. We conclude that due to the UCB algorithm, we have approximately 
# recieved 1000 more rewards as opposed to the random selection method, a direct result of exploiting the 
# optimal advert.

N = 10000
d = 10
ads_selected = []
numbers_of_selections = [0] * d
sums_of_rewards = [0] * d
total_reward = 0
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if (numbers_of_selections[i] > 0):
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            delta_i = np.sqrt(3/2 * np.log(n + 1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    total_reward = total_reward + reward
    
# Visualising the results
    
# Both charts resemble the same shape due to the more popular advert being selected more often, resulting in
# receiving more rewards.

plt.hist(ads_selected, bins=10)
plt.title('Histogram of Ads selected')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()

plt.bar(range(1,11), sums_of_rewards, color='green')
plt.title('Bar chart of Ads selected')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was rewarded')
plt.show()

'''
