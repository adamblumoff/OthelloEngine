

class SarsaLearning():
    def __init__(self, epsilon = 0.25, alpha = 0.2, gamma = 0.99):
        self.qVals = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.lastState = None
        self.lastAction = None
    def getQVals(self, state, action):
        if (state, action) in self.qVals:
            return self.qVals[(state, action)]
        return 0.0
    def getAction(self, state):
        pass