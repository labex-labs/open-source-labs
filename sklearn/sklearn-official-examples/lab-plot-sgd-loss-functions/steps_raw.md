# Convex Loss Functions Comparison

## Introduction

In machine learning, loss functions are used to measure the difference between the predicted output and the actual output. The `scikit-learn` library provides various convex loss functions for classification problems. In this lab, we will visualize and compare some of these loss functions.

## Steps

### Step 1: Import Libraries and Define Functions

We start by importing the necessary libraries and defining the modified Huber loss function.

```python
import numpy as np
import matplotlib.pyplot as plt

def modified_huber_loss(y_true, y_pred):
    z = y_pred * y_true
    loss = -4 * z
    loss[z >= -1] = (1 - z[z >= -1]) ** 2
    loss[z >= 1.0] = 0
    return loss
```

### Step 2: Define the Range for the Decision Function

We define the range of values for the decision function `f(x)`.

```python
xmin, xmax = -4, 4
xx = np.linspace(xmin, xmax, 100)
```

### Step 3: Plot the Loss Functions

We plot the various convex loss functions supported by `scikit-learn` using the `matplotlib` library.

```python
lw = 2
plt.plot([xmin, 0, 0, xmax], [1, 1, 0, 0], color="gold", lw=lw, label="Zero-one loss")
plt.plot(xx, np.where(xx < 1, 1 - xx, 0), color="teal", lw=lw, label="Hinge loss")
plt.plot(xx, -np.minimum(xx, 0), color="yellowgreen", lw=lw, label="Perceptron loss")
plt.plot(xx, np.log2(1 + np.exp(-xx)), color="cornflowerblue", lw=lw, label="Log loss")
plt.plot(xx, np.where(xx < 1, 1 - xx, 0) ** 2, color="orange", lw=lw, label="Squared hinge loss")
plt.plot(xx, modified_huber_loss(xx, 1), color="darkorchid", lw=lw, linestyle="--", label="Modified Huber loss")
plt.ylim((0, 8))
plt.legend(loc="upper right")
plt.xlabel(r"Decision function $f(x)$")
plt.ylabel("$L(y=1, f(x))$")
plt.show()
```

### Step 4: Interpret the Plot

We interpret the plot and analyze the behavior of each loss function.

## Summary

In this lab, we visualized and compared some of the convex loss functions supported by `scikit-learn`. Understanding loss functions is crucial in machine learning, as they are used to optimize the model parameters during training.
