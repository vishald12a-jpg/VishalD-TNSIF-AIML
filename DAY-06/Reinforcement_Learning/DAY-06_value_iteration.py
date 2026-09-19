import numpy as np

# Number of states
num_states = 4

# Number of actions
num_actions = 2

# Rewards
rewards = np.array([
    [0, 1],
    [0, 2],
    [1, 0],
    [10, 10]
])

# Discount factor
gamma = 0.9

# Initialize values
values = np.zeros(num_states)

# Value Iteration
for iteration in range(10):

    new_values = np.zeros(num_states)

    for state in range(num_states):

        action_values = []

        for action in range(num_actions):

            next_state = min(state + action + 1, num_states - 1)

            value = rewards[state][action] + gamma * values[next_state]

            action_values.append(value)

        new_values[state] = max(action_values)

    values = new_values

    print("Iteration", iteration + 1)
    print("Values:", values)

print("\nFinal State Values:")
print(values)