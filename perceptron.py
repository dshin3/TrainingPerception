import numpy as np
class perceptron():
    def __init__(self,X,y, threshold = 0.5, learning_rate = 0.1, max_epochs =10):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.X = X
        self.y = y
        self.max_epoche = max_epochs

    def initialize(self, init_type = 'zeros'):
       if init_type == 'random':
          self.weights = np.random.rand(len(self.X[0])) * 0.5
       if init_type == 'zeros':
          self.weights = np.zeros(len(self.X[0]))

    
    def train(self):
        '''Training function '''
        epoch = 0
        while(True):
           error_count = 0
           epoch +=1
           for (X,y) in zip(self.X, self.y):
              error_count += self.train_observation(X,y.error_count)
              if error_count == 0:
                 print("training successful")
                 break
              if epcoh >= self.max_epochs:
                 print("reached maximum epochs, no perfect prediction")
                 break

    def train_observation(self,X,y,error_count):
       ''' '''
       result = np.dot(X, self.weights) > self.threshold
       error = y - result
     


    def predict(self,X):
        ''' '''
        return int(np.dot(X, self.weights) > self.threshold)



X = [(1,0,0), (1,1,0), (1,1,1), (1,1,1), (1,0,1),(1,0,1)]
y = [1,1,0,0,1,1]

p = perceptron(X,y)
p.initialize()
p.train()
print(p.predict((1,1,1)))
print(p.predict(1,0,1))




