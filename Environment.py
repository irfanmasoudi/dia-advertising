import numpy as np

class Environment():
    def __init__(self, n_arms, probabilities): #in the environment object has characterized by 2 variables n arm and prob
        self.n_arms = n_arms #pass the input with 2 parameters and initialize the parameter
        self.probabilities = probabilities # in this case we use bernouli dist, so describe 1 value of each arm

    def round(self, pulled_arm): #model the interaction between learner and environment -> this function use the chosen arm (pulled arm) as input
        reward = np.random.binomial(1, self.probabilities[pulled_arm]) # 1 mean bernauli dist and the succes prob related to the super arm that specified in the constructor
                                    #number of trial and prob of success
        return reward
