# Novelty and Outlier Detection using scikit-learn

## Introduction

Novelty and outlier detection are techniques used to identify whether a new observation belongs to the same distribution as existing observations or if it should be considered as different. These techniques are commonly used to clean real datasets by identifying abnormal or unusual observations.

There are two important distinctions in this context:

1. Outlier detection: The training data contains outliers, which are observations that are far from the others. Outlier detection estimators try to fit the regions where the training data is the most concentrated, ignoring the deviant observations.
2. Novelty detection: The training data is not polluted by outliers, and the goal is to detect whether a new observation is an outlier. In this context, an outlier is also called a novelty.

The scikit-learn project provides a set of machine learning tools that can be used for both novelty and outlier detection. These tools are implemented using unsupervised learning algorithms, which means they learn patterns from the data without the need for labeled examples.

## Steps

### Step 1: Import the necessary libraries

First, we need to import the necessary libraries. In this example, we will use scikit-learn's `sklearn` module.

```python
from sklearn import neighbors
```

### Step 2: Load the dataset

Next, we need to load the dataset that we want to perform outlier detection on. You can use any dataset of your choice or create a custom dataset. In this example, we will use a sample dataset called `X_train`.

```python
X_train = [0.5, 1.5, 2.5, 3.5, 4.5, 10.5, 11.5, 12.5, 13.5, 14.5]
```

### Step 3: Create an outlier detection estimator

Now, we can create an outlier detection estimator object from the `neighbors.LocalOutlierFactor` class. This class implements the Local Outlier Factor algorithm, which is a popular method for outlier detection.

```python
estimator = neighbors.LocalOutlierFactor()
```

### Step 4: Fit the model to the training data

Next, we can fit the outlier detection estimator to our training data using the `fit` method.

```python
estimator.fit(X_train)
```

### Step 5: Predict outliers

Once the model is fitted, we can use the `predict` method to predict whether new observations are outliers or not. The `predict` method returns 1 for inliers and -1 for outliers.

```python
X_test = [5.5, 8.5]
predictions = estimator.predict(X_test)
print(predictions)
```

### Step 6: Access outlier scores

In addition to predicting outliers, we can also access the outlier scores for each observation using the `negative_outlier_factor_` attribute. Lower outlier scores indicate higher abnormality.

```python
outlier_scores = estimator.negative_outlier_factor_
print(outlier_scores)
```

### Summary

In this lab, we learned how to perform novelty and outlier detection using the scikit-learn library. We created an outlier detection estimator, fitted it to the training data, predicted outliers in new observations, and accessed the outlier scores. These techniques can be used to identify abnormal or unusual observations in a dataset and are commonly used for anomaly detection tasks.
