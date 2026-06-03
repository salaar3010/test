'''
# ==========================================================
# DEEP LEARNING LAB PROGRAMS
# Combined Lab 1, Lab 2, Lab 3 and Exp 4
# ==========================================================

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import torch
import torch.nn as nn


# ==========================================================
# EXPERIMENT 1
# ACTIVATION FUNCTIONS
# ==========================================================

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def softplus(x):
    return np.log(1 + np.exp(x))

def softmax(x):
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x)


activations = {
    "Sigmoid": sigmoid,
    "Tanh": tanh,
    "ReLU": relu,
    "Leaky ReLU": leaky_relu,
    "Softplus": softplus,
    "Softmax": softmax
}

print("\n========== EXPERIMENT 1 ==========")

X = np.array([3.5, 0.35, 3.5, -2.0, 1.5, -0.7])

w_init = -1
b_init = 2

for x in X:
    a = w_init * x + b_init
    h = sigmoid(a)
    print(f"Input={x:.2f}, Output={h:.4f}")

print("\nSoftmax Output:")
print(softmax(w_init * X + b_init))

a_values = np.linspace(-5, 5, 200)

plt.figure(figsize=(12, 10))

for i, (name, func) in enumerate(activations.items(), 1):
    plt.subplot(3, 2, i)
    plt.plot(a_values, func(a_values))
    plt.title(name)
    plt.grid(True)

plt.tight_layout()
plt.show()


# ==========================================================
# EXPERIMENT 2
# MCCULLOCH PITTS NEURON MODEL
# ==========================================================

print("\n========== EXPERIMENT 2 ==========")

def mcculloch_AND(inp):
    weights = np.array([1, 1])
    threshold = 2

    output = []

    for i in inp:
        if np.dot(i, weights) >= threshold:
            output.append(1)
        else:
            output.append(0)

    return output


def mcculloch_OR(inp):
    weights = np.array([1, 1])
    threshold = 1

    output = []

    for i in inp:
        if np.dot(i, weights) >= threshold:
            output.append(1)
        else:
            output.append(0)

    return output


def mcculloch_AND_NOT(inp):
    weights = np.array([1, -1])
    threshold = 1

    output = []

    for i in inp:
        if np.dot(i, weights) >= threshold:
            output.append(1)
        else:
            output.append(0)

    return output


inp = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

print("AND :", mcculloch_AND(inp))
print("OR  :", mcculloch_OR(inp))
print("AND-NOT :", mcculloch_AND_NOT(inp))


# ==========================================================
# EXPERIMENT 3
# HEBBIAN LEARNING RULE
# ==========================================================

print("\n========== EXPERIMENT 3 ==========")

x = np.array([1, -1, 1])
w = np.array([0.0, 0.0, 0.0])
y = 1

print("Initial Weights:", w)

for i in range(len(x)):
    w[i] = w[i] + x[i] * y

print("Updated Weights:", w)


# ==========================================================
# EXPERIMENT 4
# PERCEPTRON LEARNING RULE
# ==========================================================

print("\n========== EXPERIMENT 4 ==========")

x = np.array([1, 1])
target = 1

w = np.array([0.2, -0.1])

b = 1
lr = 0.1

net = np.dot(x, w) + b

if net >= 0:
    y = 1
else:
    y = -1

w = w + lr * (target - y) * x

print("Output:", y)
print("Updated Weights:", w)


# ==========================================================
# EXPERIMENT 5
# PERCEPTRON TRAINING FOR LOGIC GATES
# ==========================================================

print("\n========== EXPERIMENT 5 ==========")

def step_function(x):
    return 1 if x >= 0 else 0


def train_perceptron(X, y, gate_name):

    weights = np.zeros(2)
    bias = 0

    learning_rate = 0.1
    epochs = 5

    print(f"\n{gate_name} GATE")

    for epoch in range(epochs):

        for i in range(len(X)):

            net_input = np.dot(X[i], weights) + bias

            y_pred = step_function(net_input)

            error = y[i] - y_pred

            weights = weights + learning_rate * error * X[i]
            bias = bias + learning_rate * error

    print("Weights:", weights)
    print("Bias:", bias)

    print("Testing")

    for i in range(len(X)):
        output = step_function(np.dot(X[i], weights) + bias)
        print(X[i], "->", output)


X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

# AND
train_perceptron(
    X,
    np.array([0,0,0,1]),
    "AND"
)

# OR
train_perceptron(
    X,
    np.array([0,1,1,1]),
    "OR"
)

# NOT (Notebook version)
train_perceptron(
    X,
    np.array([0,0,1,0]),
    "NOT"
)


# ==========================================================
# EXPERIMENT 6
# FEED FORWARD NEURAL NETWORK
# L1 LOSS AND L2 LOSS
# ==========================================================

print("\n========== EXPERIMENT 6 ==========")

X = np.array([[1, 0.2, 0.8, 0.6]])
trx = torch.tensor(X, dtype=torch.float32)


class PerceptronStack(nn.Module):

    def __init__(self):
        super().__init__()

        self.lay1 = nn.Linear(4, 3)
        self.lay2 = nn.Linear(3, 2)

        self.act1 = nn.Sigmoid()
        self.act2 = nn.Softmax(dim=1)

    def forward(self, X):

        out = self.lay1(X)
        out = self.act1(out)

        out = self.lay2(out)
        out = self.act2(out)

        return out


fn = PerceptronStack()

fn.lay1.weight = nn.Parameter(torch.tensor([
    [0.6, 0.2, 0.8, 0.1],
    [0.3,-0.2, 0.8, 0.3],
    [0.8, 0.1, 0.3, 0.6]
], dtype=torch.float32))

fn.lay1.bias = nn.Parameter(
    torch.tensor([0.4, 0, -0.3], dtype=torch.float32)
)

fn.lay2.weight = nn.Parameter(torch.tensor([
    [0.2, 0.6, 0.3],
    [0.4, 0.7, 0.1]
], dtype=torch.float32))

fn.lay2.bias = nn.Parameter(
    torch.tensor([0.3, -0.2], dtype=torch.float32)
)

y_pred = fn(trx)

print("Predicted Output:")
print(y_pred)

target = torch.tensor([[0.8, 0.1]], dtype=torch.float32)

l1 = torch.abs(y_pred - target).sum()
l2 = torch.sqrt(torch.sum((y_pred - target) ** 2))

print("L1 Norm:", l1.item())
print("L2 Norm:", l2.item())


'''