# Decision Trees

## Introduction

In this lab, we will learn how to use Decision Trees for classification using scikit-learn. Decision Trees are a non-parametric supervised learning method used for classification and regression. They are simple to understand and interpret, and can handle both numerical and categorical data.

## Steps

### Step 1: Import the necessary libraries

First, we need to import the necessary libraries. We will be using scikit-learn for building and training the Decision Tree classifier.

```python
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```

### Step 2: Load the Dataset

Next, we will load the Iris dataset. This dataset contains information about four features of three different species of Iris flowers. We will use this dataset to train our Decision Tree classifier.

```python
# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
```

### Step 3: Split the Dataset

Before training the Decision Tree classifier, we need to split the dataset into training and testing sets. We will use 70% of the data for training and 30% for testing.

```python
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

### Step 4: Create and Train the Decision Tree Classifier

Now, we can create and train the Decision Tree classifier using the training data.

```python
# Create a Decision Tree classifier
clf = tree.DecisionTreeClassifier()

# Train the classifier
clf.fit(X_train, y_train)
```

### Step 5: Make Predictions

Once the classifier is trained, we can use it to make predictions on the test data.

```python
# Make predictions on the test data
y_pred = clf.predict(X_test)

# Print the predicted values
print("Predicted values:", y_pred)
```

### Step 6: Evaluate the Model

Finally, we can evaluate the accuracy of our model by comparing the predicted values with the true values.

```python
# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy
print("Accuracy:", accuracy)
```

## Summary

In this lab, we learned how to use Decision Trees for classification using scikit-learn. We loaded the Iris dataset, split the data into training and testing sets, created and trained the Decision Tree classifier, made predictions on the test data, and evaluated the accuracy of the model. Decision Trees are a powerful and interpretable method for classification tasks.
