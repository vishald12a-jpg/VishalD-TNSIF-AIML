import numpy as np
import random

# Number of states and actions
states = 5
actions = 2

# Q-table
Q = np.zeros((states, actions))

# Parameters
learning_rate = 0.8
discount_factor = 0.95
episodes = 100

# Training
for episode in range(episodes):

    state = 0

    while state != states - 1:

        # Choose random action
        action = random.randint(0, actions - 1)

        # Move to next state
        next_state = min(state + action + 1, states - 1)

        # Reward
        if next_state == states - 1:
            reward = 10
        else:
            reward = -1

        # Q-learning formula
        Q[state, action] = Q[state, action] + learning_rate * (
            reward
            + discount_factor * np.max(Q[next_state])
            - Q[state, action]
        )

        state = next_state

print("Trained Q-Table:")
print(Q)

print("\nBest action for each state:")
print(np.argmax(Q, axis=1))