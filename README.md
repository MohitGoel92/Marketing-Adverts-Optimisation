# Marketing Adverts Optimisation

**Task: Marketing advert success analysis**

We currently work for a car company in the analytics department. The marketing team has produced 10 great adverts for a new SUV but are unsure which advert to choose as their final advert to release. We wish to investigate which advert customers will respond to the best and optimise our best advert.

We will be using "Reinforcement Learning" to complete this marketing business task, with our two approaches being the "Upper Confidence Bound" and "Thompson Sampling" algorithm.

## Reinforcement Learning

Reinforcement learning is a branch of machine learning and is also referred to as "Online Learning" or "Interactive Learning". It is used to solve interacting problems where the data observed up to time T is considered to decide which action to take at time T+1. It is also used for artificial intelligence when training machines to perform tasks such as a walking robot dog. In essence the desired outcomes provide the AI machine with a reward (1), and an undesired outcome with punishment (0). Machines use this approach which enables them to learn through trial and error, a dynamic strategy.

## Upper Confidence Bound

In our task there are two main factors to consider, they are "Exploration" and "Exploitation". During exploration, our goal is to figure out which machine is the best. However, exploitation refers to maximising our results from our findings regarding the better performing advert.

In theory, we may approach this task by releasing each advert the same number of times and at the end of the experiment, the best advert will be the advert that received the most clicks. However a disadvantage of this is regret, a mathematical concept from decision theory.

**Regret**

Regret is a mathematical concept which is the consequence or amount suffered when we do not use the optimal method. Therefore, the difference between our optimal result and sub optimal result is deemed our regret. However, if we do not explore long enough we may except the sub-optimal advert as our optimal advert.

We wish to combine exploration and exploitation together and get to the optimal solution as soon as we can to maximise the output of our efforts.

In the dataset under study, we have 10 columns that represent our 10 adverts, and 10,000 rows which represent 10,000 rounds. The dataset contains 0's and 1's which represent whether a customer would have selected that advert (1) or not (0), if that advert was shown to that person. Each person is represented by a round n (1 of 10,000).

**Steps for applying the Upper Confidence Bound algorithm**

- **Step 1:** At each round n, we consider two numbers for each ad i:

  <img src = 'Screen3.png' width='700'>

- **Step 2:** From these two numbers we compute:

  <img src = 'Screen7.png' width='700'>

- **Step 3:** We select the ad i that has the maximum upper confidence bound
  
  <img src = 'Screen8.png' width='200'>
