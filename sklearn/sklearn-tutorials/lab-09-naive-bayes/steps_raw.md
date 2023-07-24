# Naive Bayes Example

## Introduction

In this lab, we will go through an example of using Naive Bayes classifiers from the scikit-learn library in Python. Naive Bayes classifiers are a set of supervised learning algorithms that are commonly used for classification tasks. These classifiers are based on applying Bayes' theorem with the assumption of conditional independence between every pair of features given the value of the class variable.

In this example, we will use the Gaussian Naive Bayes classifier from scikit-learn to classify the iris dataset, which is a popular dataset for machine learning. The goal is to predict the species of an iris flower based on its petal and sepal dimensions.

## Steps

### Step 1: Import Libraries and Load the Dataset

Let's start by importing the necessary libraries and loading the iris dataset. We will use the `load_iris` function from the `sklearn.datasets` module to load the dataset.

```python
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Target variable

print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])
print("Number of classes:", len(set(y)))
```

### Step 2: Split the Dataset into Training and Test Sets

Next, we will split the dataset into training and test sets using the `train_test_split` function from the `sklearn.model_selection` module. The training set will be used to train the Naive Bayes classifier, and the test set will be used to evaluate its performance.

```python
from sklearn.model_selection import train_test_split

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### Step 3: Train and Evaluate the Gaussian Naive Bayes Classifier

Now, we will train the Gaussian Naive Bayes classifier on the training set and evaluate its performance on the test set. We will use the `GaussianNB` class from the `sklearn.naive_bayes` module.

```python
from sklearn.naive_bayes import GaussianNB

# Create a Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Train the classifier
gnb.fit(X_train, y_train)

# Predict the target variable for the test set
y_pred = gnb.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = (y_pred == y_test).sum() / len(y_test)
print("Accuracy:", accuracy)
```

### Step 4: Interpret the Results

Based on the accuracy obtained, we can interpret the performance of the Gaussian Naive Bayes classifier on the iris dataset. The accuracy represents the proportion of correctly predicted target variable values in the test set. In this case, the accuracy represents the proportion of correctly classified iris flower species.

## Summary

In this lab, we went through an example of using the Gaussian Naive Bayes classifier from scikit-learn. We loaded the iris dataset, split it into training and test sets, trained the classifier on the training set, and evaluated its performance on the test set. The accuracy obtained gives us an indication of how well the classifier performed in predicting the species of iris flowers. Naive Bayes classifiers are simple yet effective algorithms for classification tasks and are commonly used in various real-world applications.
