# Marketing Adverts Optimisation

**Task: Marketing advert success analysis**

We currently work for a car company in the analytics department. The marketing team has produced 10 great adverts for a new SUV but are unsure which advert to choose as their final advert to release. We wish to investigate which advert customers will respond to the best and optimise our best advert.

We will be using "Reinforcement Learning" to complete this marketing business task, with our two approaches being the "Upper Confidence Bound" and "Thompson Sampling" algorithm.

## Reinforcement Learning

Reinforcement learning is a branch of machine learning and is also referred to as "Online Learning" or "Interactive Learning". It is used to solve interacting problems where the data observed up to time T is considered to decide which action to take at time T+1. It is also used for artificial intelligence when training machines to perform tasks such as a walking robot dog. In essence the desired outcomes provide the AI machine with a reward (1), and an undesired outcome with punishment (0). Machines use this approach which enables them to learn through trial and error, a dynamic strategy.

## Upper Confidence Bound

In our task there are two main factors we must consider, they are "Exploration" and "Exploitation". During exploration, our goal is to figure out which machine is the best. However, exploitation refers to maximising our results from our findings regarding the better performing advert.

In theory, we may approach this task by releasing each advert the same number of times and at the end of the experiment, the best advert will be the advert that received the most clicks. However a disadvantage of this is regret, a mathematical concept from decision theory.

**Regret**

Regret is a mathematical concept which is the consequence or amount suffered when we do not use the optimal method. Therefore, the difference between our optimal result and sub optimal result is deemed our regret. However, if we do not explore long enough we may except the sub-optimal advert as our optimal advert.

