# Active Learning with Label Propagation

## Introduction

This lab demonstrates an active learning technique to learn handwritten digits using label propagation. The Label Propagation is a semi-supervised learning method that uses a graph-based approach to propagate labels across data points. Active learning is a process that allows us to iteratively select data points to label, and use these labeled points to retrain the model.

## Steps

### Step 1: Load the Digits Dataset

We will start by loading the digits dataset from scikit-learn library.

```python
from sklearn import datasets

digits = datasets.load_digits()
```

### Step 2: Shuffle and Split Data

Next, we will shuffle and split the dataset into labeled and unlabeled parts. We will start with only 10 labeled points.

```python
import numpy as np

rng = np.random.RandomState(0)
indices = np.arange(len(digits.data))
rng.shuffle(indices)

X = digits.data[indices[:330]]
y = digits.target[indices[:330]]
images = digits.images[indices[:330]]

n_total_samples = len(y)
n_labeled_points = 10
unlabeled_indices = np.arange(n_total_samples)[n_labeled_points:]
```

### Step 3: Train Label Propagation Model

We will now train a label propagation model with the labeled data points and use it to predict the labels of the remaining unlabeled data points.

```python
from sklearn.semi_supervised import LabelSpreading

lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
predicted_labels = lp_model.transduction_[unlabeled_indices]
```

### Step 4: Select Most Uncertain Points

We will select the top five most uncertain points based on their predicted label distributions and request human labels for them.

```python
from scipy import stats

pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
uncertainty_index = np.argsort(pred_entropies)[::-1]
uncertainty_index = uncertainty_index[np.in1d(uncertainty_index, unlabeled_indices)][:5]
```

### Step 5: Label the Most Uncertain Points

We will add the human labels to the labeled data points and train the model with them.

```python
y_train[uncertainty_index] = y[uncertainty_index]
lp_model.fit(X, y_train)
```

### Step 6: Repeat

We will repeat the process of selecting the top five most uncertain points, adding their labels to the labeled data points, and training the model until we have 30 labeled data points.

```python
max_iterations = 3

for i in range(max_iterations):
    if len(unlabeled_indices) == 0:
        print("No unlabeled items left to label.")
        break

    # select top five uncertain points
    pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
    uncertainty_index = np.argsort(pred_entropies)[::-1]
    uncertainty_index = uncertainty_index[np.in1d(uncertainty_index, unlabeled_indices)][:5]

    # add labels to labeled data points
    y_train[uncertainty_index] = y[uncertainty_index]

    # train the model
    lp_model.fit(X, y_train)

    # remove labeled data points from the unlabeled set
    delete_indices = np.array([], dtype=int)
    for index, image_index in enumerate(uncertainty_index):
        (delete_index,) = np.where(unlabeled_indices == image_index)
        delete_indices = np.concatenate((delete_indices, delete_index))
    unlabeled_indices = np.delete(unlabeled_indices, delete_indices)
    n_labeled_points += len(uncertainty_index)
```

## Summary

In summary, this lab demonstrated an active learning technique using Label Propagation to learn handwritten digits. We started by training a label propagation model with only 10 labeled points, and iteratively selected the top five most uncertain points to label until we had 30 labeled data points. This active learning technique can be useful to minimize the number of labeled data points required to train a model while maximizing its performance.
