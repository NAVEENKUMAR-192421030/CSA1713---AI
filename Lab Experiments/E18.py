import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Input values
x1 = 1
x2 = 0

# Weights
w1 = 0.5
w2 = 0.4
w3 = 0.3
w4 = 0.2

# Hidden layer
h1 = sigmoid(x1 * w1 + x2 * w2)
h2 = sigmoid(x1 * w3 + x2 * w4)

# Output layer
output = sigmoid(h1 * 0.6 + h2 * 0.7)

print("Feed Forward Neural Network")
print("Hidden Layer Output 1:", h1)
print("Hidden Layer Output 2:", h2)
print("Final Output:", output)
