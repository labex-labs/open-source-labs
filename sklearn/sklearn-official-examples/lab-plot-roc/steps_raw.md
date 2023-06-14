# Multiclass ROC Evaluation with Scikit-learn

## Introduction

This lab demonstrates the use of Receiver Operating Characteristic (ROC) metric to evaluate the quality of multiclass classifiers using Scikit-learn library.

## Steps

1. **Load and Prepare the Data**: In this step, we load the iris dataset which contains 3 classes and prepare it for the evaluation of a classifier using the ROC metric.

2. **One-vs-Rest Multiclass ROC**: This step shows how to calculate the ROC curve using the One-vs-Rest (OvR) multiclass strategy.

3. **One-vs-One Multiclass ROC**: In this step, we calculate the ROC curve using the One-vs-One (OvO) multiclass strategy.

### Step 1: Load and Prepare the Data

Let's start by loading the iris dataset and preparing it for the evaluation of a classifier using the ROC metric.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
target_names = iris.target_names
X, y = iris.data, iris.target
y = iris.target_names[y]

# Add noisy features to make the problem harder
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
n_classes = len(np.unique(y))
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, stratify=y, random_state=0)
```

### Step 2: One-vs-Rest Multiclass ROC

The One-vs-the-Rest (OvR) multiclass strategy consists of computing a ROC curve per each of the `n_classes`. In each step, a given class is regarded as the positive class and the remaining classes are regarded as the negative class as a bulk. In this step, we show how to calculate the ROC curve using the OvR multiclass strategy.

```python
from sklearn.preprocessing import LabelBinarizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay

# Binarize the target using the OvR strategy
label_binarizer = LabelBinarizer().fit(y_train)
y_onehot_test = label_binarizer.transform(y_test)

# Train a Logistic Regression model
classifier = LogisticRegression()
y_score = classifier.fit(X_train, y_train).predict_proba(X_test)

# Calculate ROC curve and ROC AUC score for each class
fpr, tpr, roc_auc = dict(), dict(), dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_onehot_test[:, i], y_score[:, i])
    roc_auc[i] = roc_auc_score(y_onehot_test[:, i], y_score[:, i])

# Compute micro-average ROC curve and ROC area
fpr["micro"], tpr["micro"], _ = roc_curve(y_onehot_test.ravel(), y_score.ravel())
roc_auc["micro"] = roc_auc_score(y_onehot_test, y_score, multi_class="ovr", average="micro")

# Compute macro-average ROC curve and ROC area
# Aggregate the true/false positive rates per class
fpr["macro"], tpr["macro"] = [], []
for i in range(n_classes):
    fpr_averaged, tpr_averaged = [], []
    for j in range(n_classes):
        if i != j:
            fpr_averaged += list(fpr[j])
            tpr_averaged += list(tpr[j])
    fpr_averaged = np.array(fpr_averaged)
    tpr_averaged = np.array(tpr_averaged)
    fpr["macro"].append(fpr_averaged)
    tpr["macro"].append(tpr_averaged)
fpr["macro"] = np.concatenate(fpr["macro"])
tpr["macro"] = np.concatenate(tpr["macro"])
roc_auc["macro"] = roc_auc_score(y_onehot_test, y_score, multi_class="ovr", average="macro")

# Plot ROC curves for each class and the micro/macro averages
fig, ax = plt.subplots(figsize=(6, 6))
colors = ["aqua", "darkorange", "cornflowerblue"]
for i, color in zip(range(n_classes), colors):
    RocCurveDisplay.from_predictions(
        y_onehot_test[:, i],
        y_score[:, i],
        name=f"ROC curve of class {target_names[i]} (AUC = {roc_auc[i]:.2f})",
        color=color,
        ax=ax,
        plot_micro=False,
        plot_macro=False,
    )

RocCurveDisplay.from_predictions(
    y_onehot_test.ravel(),
    y_score.ravel(),
    name=f"Micro-average ROC curve (AUC = {roc_auc['micro']:.2f})",
    color="deeppink",
    linestyle=":",
    linewidth=4,
    ax=ax,
)

plt.plot(
    fpr["macro"],
    tpr["macro"],
    label=f"Macro-average ROC curve (AUC = {roc_auc['macro']:.2f})",
    color="navy",
    linestyle=":",
    linewidth=4,
)

plt.plot([0, 1], [0, 1], "k--", label="Chance level")
plt.axis("square")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("One-vs-Rest ROC curves")
plt.legend()
plt.show()
```

### Step 3: One-vs-One Multiclass ROC

The One-vs-One (OvO) multiclass strategy consists of fitting one classifier per class pair. Since it requires to train `n_classes` \* (`n_classes` - 1) / 2 classifiers, this method is usually slower than One-vs-Rest due to its O(`n_classes` ^2) complexity. In this step, we show how to calculate the ROC curve using the OvO multiclass strategy.

```python
pair_list = [(0, 1), (1, 2), (0, 2)]
pair_scores = []
mean_tpr = dict()

# Compute ROC curve and ROC AUC score for each pair of classes
for ix, (label_a, label_b) in enumerate(pair_list):
    a_mask = y_test == target_names[label_a]
    b_mask = y_test == target_names[label_b]
    ab_mask = np.logical_or(a_mask, b_mask)

    a_true = a_mask[ab_mask]
    b_true = b_mask[ab_mask]

    idx_a = np.flatnonzero(label_binarizer.classes_ == target_names[label_a])[0]
    idx_b = np.flatnonzero(label_binarizer.classes_ == target_names[label_b])[0]

    fpr_a, tpr_a, _ = roc_curve(a_true, y_score[ab_mask, idx_a])
    fpr_b, tpr_b, _ = roc_curve(b_true, y_score[ab_mask, idx_b])

    mean_tpr[ix] = np.zeros_like(fpr_grid)
    mean_tpr[ix] += np.interp(fpr_grid, fpr_a, tpr_a)
    mean_tpr[ix] += np.interp(fpr_grid, fpr_b, tpr_b)
    mean_tpr[ix] /= 2
    mean_score = auc(fpr_grid, mean_tpr[ix])
    pair_scores.append(mean_score)

    fig, ax = plt.subplots(figsize=(6, 6))
    plt.plot(
        fpr_grid,
        mean_tpr[ix],
        label=f"Mean {target_names[label_a]} vs {target_names[label_b]} (AUC = {mean_score :.2f})",
        linestyle=":",
        linewidth=4,
    )
    RocCurveDisplay.from_predictions(
        a_true,
        y_score[ab_mask, idx_a],
        ax=ax,
        name=f"{target_names[label_a]} as positive class",
    )
    RocCurveDisplay.from_predictions(
        b_true,
        y_score[ab_mask, idx_b],
        ax=ax,
        name=f"{target_names[label_b]} as positive class",
        plot_chance_level=True,
    )
    plt.axis("square")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(f"{target_names[idx_a]} vs {target_names[idx_b]} ROC curves")
    plt.legend()
    plt.show()

# Compute macro-average ROC curve and ROC AUC score
mean_tpr = np.zeros_like(fpr_grid)
for ix in range(len(pair_list)):
    mean_tpr += mean_tpr[ix]
mean_tpr /= len(pair_list)

macro_roc_auc_ovo = roc_auc_score(y_test, y_score, multi_class="ovo", average="macro")

plt.plot(
    fpr_grid,
    mean_tpr,
    label=f"Macro-average ROC curve (AUC = {macro_roc_auc_ovo:.2f})",
    linestyle=":",
    linewidth=4,
)

plt.plot([0, 1], [0, 1], "k--", label="Chance level")
plt.axis("square")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("One-vs-One ROC curves")
plt.legend()
plt.show()
```

## Summary

In this lab, we learned how to evaluate the performance of a multiclass classifier using the ROC curve and ROC AUC score. We demonstrated how to calculate ROC curves using the One-vs-Rest (OvR) and One-vs-One (OvO) multiclass strategies. We also showed how to calculate micro and macro-averaged ROC curves and ROC AUC scores using Scikit-learn.
