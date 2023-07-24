# Logistic Regression Classifier on Iris Dataset

## Introduction

In this lab, we will use Logistic Regression Classifier to classify the first two features of Iris dataset based on their labels. We will use scikit-learn library to load and preprocess the dataset, create an instance of Logistic Regression Classifier, and fit the data. Finally, we will display the decision boundaries on the scatter plot.

## Steps

### Step 1: Load the Dataset and Preprocess

We will use scikit-learn library to load the Iris dataset. The dataset contains 3 classes of 50 instances each, where each class refers to a type of iris plant. Each instance has 4 features: sepal length, sepal width, petal length, and petal width.

```python
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay

# load the Iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
Y = iris.target
```

### Step 2: Create an Instance of Logistic Regression Classifier and Fit the Data

We will create an instance of Logistic Regression Classifier and fit the data.

```python
# Create an instance of Logistic Regression Classifier and fit the data.
logreg = LogisticRegression(C=1e5)
logreg.fit(X, Y)
```

### Step 3: Display the Decision Boundaries on the Scatter Plot

We will display the decision boundaries on the scatter plot using DecisionBoundaryDisplay from scikit-learn library.

```python
_, ax = plt.subplots(figsize=(4, 3))
DecisionBoundaryDisplay.from_estimator(
    logreg,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    shading="auto",
    xlabel="Sepal length",
    ylabel="Sepal width",
    eps=0.5,
)

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors="k", cmap=plt.cm.Paired)

plt.xticks(())
plt.yticks(())

plt.show()
```

## Summary

In this lab, we used Logistic Regression Classifier to classify the first two features of Iris dataset based on their labels. We loaded and preprocessed the dataset using scikit-learn library, created an instance of Logistic Regression Classifier, and fit the data. Finally, we displayed the decision boundaries on the scatter plot.
