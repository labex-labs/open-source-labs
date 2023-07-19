# Early Stopping of Gradient Boosting

## Introduction

Gradient boosting is an ensemble technique where several weak learners (regression trees) are combined to yield a powerful single model, in an iterative fashion. Early stopping support in Gradient Boosting enables us to find the least number of iterations which is sufficient to build a model that generalizes well to unseen data.

## Steps

### Step 1: Load the Required Libraries and Data

First, we need to load the required libraries and data. We will use the scikit-learn library for the implementation of gradient boosting.

```python
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import ensemble
from sklearn import datasets
from sklearn.model_selection import train_test_split

data_list = [
    datasets.load_iris(return_X_y=True),
    datasets.make_classification(n_samples=800, random_state=0),
    datasets.make_hastie_10_2(n_samples=2000, random_state=0),
]
names = ["Iris Data", "Classification Data", "Hastie Data"]
n_estimators = 200
```

### Step 2: Prepare the Data

Next, we will prepare the data by splitting it into training and testing sets.

```python
for X, y in data_list:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )
```

### Step 3: Build and Train the Model without Early Stopping

We will now build and train a gradient boosting model without early stopping.

```python
gb = ensemble.GradientBoostingClassifier(n_estimators=n_estimators, random_state=0)
start = time.time()
gb.fit(X_train, y_train)
time_gb.append(time.time() - start)
```

### Step 4: Build and Train the Model with Early Stopping

We will now build and train a gradient boosting model with early stopping. We specify a validation*fraction which denotes the fraction of the whole dataset that will be kept aside from training to assess the validation loss of the model. The gradient boosting model is trained using the training set and evaluated using the validation set. When each additional stage of regression tree is added, the validation set is used to score the model. This is continued until the scores of the model in the last n_iter_no_change stages do not improve by at least tol. After that, the model is considered to have converged and further addition of stages is "stopped early". The number of stages of the final model is available at the attribute n_estimators*.

```python
gbes = ensemble.GradientBoostingClassifier(
        n_estimators=n_estimators,
        validation_fraction=0.2,
        n_iter_no_change=5,
        tol=0.01,
        random_state=0,
    )
start = time.time()
gbes.fit(X_train, y_train)
time_gbes.append(time.time() - start)
```

### Step 5: Compare Scores with and without Early Stopping

We will now compare the scores of the two models.

```python
score_gb.append(gb.score(X_test, y_test))
score_gbes.append(gbes.score(X_test, y_test))
```

### Step 6: Compare Fit Times with and without Early Stopping

We will now compare the fit times of the two models.

```python
plt.figure(figsize=(9, 5))

bar1 = plt.bar(
    index, time_gb, bar_width, label="Without early stopping", color="crimson"
)
bar2 = plt.bar(
    index + bar_width, time_gbes, bar_width, label="With early stopping", color="coral"
)

max_y = np.amax(np.maximum(time_gb, time_gbes))

plt.xticks(index + bar_width, names)
plt.yticks(np.linspace(0, 1.3 * max_y, 13))

autolabel(bar1, n_gb)
autolabel(bar2, n_gbes)

plt.ylim([0, 1.3 * max_y])
plt.legend(loc="best")
plt.grid(True)

plt.xlabel("Datasets")
plt.ylabel("Fit Time")

plt.show()
```

### Step 7: Compare Scores with and without Early Stopping

We will now compare the scores of the two models.

```python
plt.figure(figsize=(9, 5))

bar1 = plt.bar(
    index, score_gb, bar_width, label="Without early stopping", color="crimson"
)
bar2 = plt.bar(
    index + bar_width, score_gbes, bar_width, label="With early stopping", color="coral"
)

plt.xticks(index + bar_width, names)
plt.yticks(np.arange(0, 1.3, 0.1))

autolabel(bar1, n_gb)
autolabel(bar2, n_gbes)

plt.ylim([0, 1.3])
plt.legend(loc="best")
plt.grid(True)

plt.xlabel("Datasets")
plt.ylabel("Test score")

plt.show()
```

## Summary

In this lab, we learned about early stopping in gradient boosting, which enables us to find the least number of iterations that are sufficient to build a model that generalizes well to unseen data. We compared the performance of a gradient boosting model with and without early stopping, and observed that early stopping can significantly reduce training time, memory usage, and prediction latency.
