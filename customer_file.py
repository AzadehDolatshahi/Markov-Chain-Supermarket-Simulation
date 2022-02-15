import pandas as pd
import random

df=pd.read_csv('transition_matrix.csv', index_col=0)
# All transition states
transition_matrix = df.to_dict(orient='index')
for key in transition_matrix.keys():
    transition_matrix[key] = list(transition_matrix[key].values())

STATES_ALL = ['checkout','dairy','drinks','fruit','spices']
TRANSITION_MATRIX_ALL = transition_matrix
STATES_START = ['dairy','drinks','fruit','spices']

class CustomerClass:
    def __init__(self):
        self.history = random.choices(STATES_START)             # first state shall not be checkout, so a random choice from the other states is made 

    # gets next state based on the transition matrix probabilities until checkout is reached
    def next_state(self):
        first_state= self.history[0] 
        next_state='fruit'
        while next_state != ['checkout']:
            next_state = random.choices(STATES_ALL, weights=TRANSITION_MATRIX_ALL[first_state])
            self.history.append(next_state[0])
            if next_state == 'check_out':
                break
        return self.history


