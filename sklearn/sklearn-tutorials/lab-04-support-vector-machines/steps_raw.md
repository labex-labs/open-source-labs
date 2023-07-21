# Support Vector Machines

## Introduction

In this tutorial, we will learn about Support Vector Machines (SVM), which are a set of supervised learning methods used for classification, regression, and outlier detection. SVMs are effective in high-dimensional spaces and can still perform well when the number of dimensions is greater than the number of samples.

The advantages of SVMs include their effectiveness in high-dimensional spaces, memory efficiency, and versatility in terms of different kernel functions. However, it is important to avoid overfitting and choose the right kernel and regularization term for the given problem.

In this tutorial, we will cover the following topics:

1. Classification with SVM
2. Multi-class classification
3. Scores and probabilities
4. Unbalanced problems
5. Regression with SVM
6. Density estimation and novelty detection

## Steps

### Step 1: Classification with SVM

- Start by importing the necessary libraries:

```python
from sklearn import svm
```

- Define the training samples `X` and class labels `y`:

```python
X = [[0, 0], [1, 1]]
y = [0, 1]
```

- Create an instance of the `SVC` classifier and fit the data:

```python
clf = svm.SVC()
clf.fit(X, y)
```

- Use the trained model to predict new values:

```python
clf.predict([[2., 2.]])
```

### Step 2: Multi-class Classification

- The `SVC` and `NuSVC` classifiers can be used for multi-class classification using the "one-versus-one" approach:

```python
X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, Y)
dec = clf.decision_function([[1]])
```

### Step 3: Scores and Probabilities

- SVMs do not directly provide probability estimates, but you can enable probability estimation by setting the `probability` parameter to `True`:

```python
clf = svm.SVC(probability=True)
clf.fit(X, y)
```

- You can then use the `predict_proba` method to get the probabilities of each class:

```python
clf.predict_proba([[2., 2.]])
```

- Note that probability estimation is expensive and requires cross-validation, so use it judiciously.

### Step 4: Unbalanced Problems

- SVMs can handle unbalanced problems by adjusting the `class_weight` parameter:

```python
clf = svm.SVC(class_weight={1: 10})
clf.fit(X, y)
```

### Step 5: Regression with SVM

- For regression problems, SVMs can be used with the `SVR` class:

```python
X = [[0, 0], [1, 1]]
y = [0.5, 2.5]
regr = svm.SVR()
regr.fit(X, y)
regr.predict([[1, 1]])
```

### Step 6: Density Estimation and Novelty Detection

- SVMs can also be used for density estimation and novelty detection with the `OneClassSVM` class:

```python
clf = svm.OneClassSVM()
clf.fit(X)
clf.predict(X)
```

## Summary

In this tutorial, we learned about Support Vector Machines (SVM) and its applications in classification, regression, density estimation, and novelty detection. We covered the steps for classification, multi-class classification, scores and probabilities, unbalanced problems, regression, and density estimation. SVMs are powerful tools for machine learning and can be used in various scenarios to achieve accurate predictions.
