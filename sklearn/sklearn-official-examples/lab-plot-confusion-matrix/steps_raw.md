# Scikit-Learn Confusion Matrix Tutorial

## Introduction

The confusion matrix is a tool for evaluating the performance of a classification algorithm. It is a table that summarizes the performance of a classification model by comparing predicted class labels with actual class labels. This tutorial demonstrates how to use the scikit-learn library to generate a confusion matrix and visualize its results.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries. We will use scikit-learn, matplotlib, numpy, and datasets.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
```

### Step 2: Load Data

We will use the iris dataset from scikit-learn. The dataset contains 150 samples, each with four features and a target label.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
```

### Step 3: Split Data

We will split the dataset into a training set and a test set. The training set will be used to train the model, and the test set will be used to evaluate the model's performance.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```

### Step 4: Train Model

We will train a support vector machine (SVM) classifier using a linear kernel. We will use a regularization parameter C that is too low to see the impact on the results.

```python
classifier = svm.SVC(kernel="linear", C=0.01).fit(X_train, y_train)
```

### Step 5: Generate Confusion Matrix

We will generate a confusion matrix using the ConfusionMatrixDisplay class from scikit-learn. The confusion matrix will show the number of correct and incorrect predictions for each class.

```python
np.set_printoptions(precision=2)
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    X_test,
    y_test,
    display_labels=class_names,
    cmap=plt.cm.Blues,
    normalize=None,
)
```

### Step 6: Visualize Confusion Matrix

We will visualize the confusion matrix using matplotlib. We will plot both a non-normalized confusion matrix and a normalized confusion matrix.

```python
titles_options = [
    ("Confusion matrix, without normalization", None),
    ("Normalized confusion matrix", "true"),
]
for title, normalize in titles_options:
    disp = ConfusionMatrixDisplay.from_estimator(
        classifier,
        X_test,
        y_test,
        display_labels=class_names,
        cmap=plt.cm.Blues,
        normalize=normalize,
    )
    disp.ax_.set_title(title)
    print(title)
    print(disp.confusion_matrix)
plt.show()
```

## Summary

In this tutorial, we learned how to use the scikit-learn library to generate a confusion matrix and visualize its results. We loaded the iris dataset, split it into training and test sets, trained a support vector machine classifier, and generated and visualized a confusion matrix. The confusion matrix showed the number of correct and incorrect predictions for each class, and the visualization helped us to interpret the results.
