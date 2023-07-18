# Digits Classification

## Introduction

This lab is a step-by-step tutorial on how to use classification techniques on the Digits dataset using scikit-learn. In this lab, we will load the dataset, preprocess the data, split the dataset into training and testing sets, and then use two different classification techniques (K-Nearest Neighbors and Logistic Regression) to classify the digits. Finally, we will compare the accuracy of both techniques.

## Steps

### Step 1: Load the Digits dataset

We will start by loading the digits dataset using the `load_digits` function from scikit-learn. This function returns two arrays: `X_digits` containing the input data and `y_digits` containing the target labels.

```python
from sklearn import datasets

X_digits, y_digits = datasets.load_digits(return_X_y=True)
```

### Step 2: Preprocess the data

We will then preprocess the data by scaling the features to a range of [0, 1] using the maximum value of the data. This can be done by dividing the input data by the maximum value of the input data.

```python
X_digits = X_digits / X_digits.max()
```

### Step 3: Split the dataset into training and testing sets

Next, we will split the dataset into training and testing sets using scikit-learn's `train_test_split` function. We will use 90% of the data for training and 10% for testing.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_digits, y_digits, test_size=0.1, random_state=42)
```

### Step 4: Train and test the K-Nearest Neighbors classifier

We will now train a K-Nearest Neighbors (KNN) classifier using scikit-learn's `KNeighborsClassifier` function and test it on the testing set. We will then print the accuracy score of the classifier.

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
knn_score = knn.score(X_test, y_test)

print("KNN score: %f" % knn_score)
```

### Step 5: Train and test the Logistic Regression classifier

We will now train a Logistic Regression classifier using scikit-learn's `LogisticRegression` function and test it on the testing set. We will then print the accuracy score of the classifier.

```python
from sklearn.linear_model import LogisticRegression

logistic = LogisticRegression(max_iter=1000)
logistic.fit(X_train, y_train)
logistic_score = logistic.score(X_test, y_test)

print("Logistic Regression score: %f" % logistic_score)
```

### Step 6: Compare the accuracy of both classifiers

Finally, we will compare the accuracy of both classifiers by printing the accuracy scores of both classifiers.

```python
print("KNN score: %f" % knn_score)
print("Logistic Regression score: %f" % logistic_score)
```

## Summary

In this lab, we learned how to use classification techniques on the Digits dataset using scikit-learn. We loaded the dataset, preprocessed the data, split the dataset into training and testing sets, and then trained and tested two different classifiers (K-Nearest Neighbors and Logistic Regression) on the testing set. Finally, we compared the accuracy of both classifiers.
