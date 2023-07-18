# Scikit-Learn make_multilabel_classification Tutorial

## Introduction

In this lab, we will learn how to generate a multilabel dataset using the `make_multilabel_classification` function of Scikit-Learn library. The function generates random samples of multilabel data, where each sample has counts of two features, which are differently distributed in each of two classes.

## Steps

### Step 1: Import Required Libraries and Define Constants

First, we need to import the required libraries and define the colors and random seed constant for generating the multilabel dataset.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification as make_ml_clf

COLORS = np.array(
    [
        "!",
        "#FF3333",  # red
        "#0198E1",  # blue
        "#BF5FFF",  # purple
        "#FCD116",  # yellow
        "#FF7216",  # orange
        "#4DBD33",  # green
        "#87421F",  # brown
    ]
)

# Use same random seed for multiple calls to make_multilabel_classification to
# ensure same distributions
RANDOM_SEED = np.random.randint(2**10)
```

### Step 2: Define the Plot Function

Next, we define a function `plot_2d` that plots the randomly generated multilabel dataset. It takes three arguments `n_labels`, `n_classes`, and `length`.

```python
def plot_2d(ax, n_labels=1, n_classes=3, length=50):
    X, Y, p_c, p_w_c = make_ml_clf(
        n_samples=150,
        n_features=2,
        n_classes=n_classes,
        n_labels=n_labels,
        length=length,
        allow_unlabeled=False,
        return_distributions=True,
        random_state=RANDOM_SEED,
    )

    ax.scatter(
        X[:, 0], X[:, 1], color=COLORS.take((Y * [1, 2, 4]).sum(axis=1)), marker="."
    )
    ax.scatter(
        p_w_c[0] * length,
        p_w_c[1] * length,
        marker="*",
        linewidth=0.5,
        edgecolor="black",
        s=20 + 1500 * p_c**2,
        color=COLORS.take([1, 2, 4]),
    )
    ax.set_xlabel("Feature 0 count")
    return p_c, p_w_c
```

This function generates the dataset using the `make_multilabel_classification` function with the specified parameters. Then, it plots the dataset using the `scatter` function of Matplotlib library. The function returns the class probabilities and feature probabilities.

### Step 3: Plot the Dataset

Now, we plot the randomly generated multilabel dataset using the `plot_2d` function. We create a figure with two subplots and call the `plot_2d` function for each subplot with different parameter values.

```python
_, (ax1, ax2) = plt.subplots(1, 2, sharex="row", sharey="row", figsize=(8, 4))
plt.subplots_adjust(bottom=0.15)

p_c, p_w_c = plot_2d(ax1, n_labels=1)
ax1.set_title("n_labels=1, length=50")
ax1.set_ylabel("Feature 1 count")

plot_2d(ax2, n_labels=3)
ax2.set_title("n_labels=3, length=50")
ax2.set_xlim(left=0, auto=True)
ax2.set_ylim(bottom=0, auto=True)

plt.show()
```

### Step 4: Print the Class and Feature Probabilities

Lastly, we print the class and feature probabilities for each class using the class probabilities and feature probabilities returned by the `plot_2d` function.

```python
print("The data was generated from (random_state=%d):" % RANDOM_SEED)
print("Class", "P(C)", "P(w0|C)", "P(w1|C)", sep="\t")
for k, p, p_w in zip(["red", "blue", "yellow"], p_c, p_w_c.T):
    print("%s\t%0.2f\t%0.2f\t%0.2f" % (k, p, p_w[0], p_w[1]))
```

## Summary

In this lab, we learned how to generate a multilabel dataset using the `make_multilabel_classification` function of Scikit-Learn library. We also learned how to plot the dataset and print the class and feature probabilities.
