import numpy as np
import pandas as pd
import random


class MyLinearRegression:
    def __init__(self, x, y, learning_rate):
        if isinstance(x, pd.DataFrame):
            x = x.values
        if isinstance(y, pd.Series):
            y = y.values

        self.x = x
        self.y = y
        self.learning_rate = learning_rate
        typeChecks()

    
    def typeChecks(self):
        if not isinstance(self.x, np.ndarray):
            raise("x should be numpy array")

        if not isinstance(self.y, np.ndarray):
            raise("y should be numpy array")

        if not isinstance(self.learning_rate, float):
            raise("learning_rate should be numeric")


    def cost(self):
        rows = self.x.shape[0]
        columns = self.x.shape[1]

        bias_coeff = np.ones(rows)
        thetas = np.random.uniform(0,100,(columns+1))
        





