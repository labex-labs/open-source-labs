# Neural Network Models

## Introduction

In this lab, we will learn about neural network models and how they can be used in supervised learning tasks. Neural networks are a popular type of machine learning algorithm that can learn non-linear patterns in data. They are often used for classification and regression tasks.

We will specifically focus on the Multi-layer Perceptron (MLP) algorithm, which is a type of neural network that has one or more hidden layers between the input and output layers. MLP can learn complex non-linear relationships in data, making it suitable for a wide range of tasks.

## Steps

### Step 1: Import the necessary libraries

```python
from sklearn.neural_network import MLPClassifier
```

### Step 2: Load the dataset

```python
# Load the dataset
X = [[0., 0.], [1., 1.]]
y = [0, 1]
```

### Step 3: Create and train the MLP model

```python
# Create an MLP classifier with one hidden layer of 5 neurons
clf = MLPClassifier(hidden_layer_sizes=(5,), random_state=1)

# Train the model using the training data
clf.fit(X, y)
```

### Step 4: Make predictions with the trained model

```python
# Make predictions for new samples
predictions = clf.predict([[0., 1.], [1., 0.]])
```

### Step 5: Evaluate the model

```python
# Evaluate the model accuracy
accuracy = clf.score(X, y)
```

## Summary

In this lab, we learned about neural network models, specifically the Multi-layer Perceptron (MLP) algorithm. We imported the necessary libraries, loaded the dataset, created and trained an MLP model, made predictions with the trained model, and evaluated the model's accuracy.

MLP is a powerful algorithm that can learn non-linear patterns in data and is widely used for classification and regression tasks. It can be a useful tool in your machine learning toolbox.
