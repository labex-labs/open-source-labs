# LinearSVC Support Vectors

## Introduction

Support Vector Machines (SVM) is a popular machine learning algorithm used for classification and regression analysis. SVM tries to find the best possible boundary that separates different classes of data. In this lab, we will learn how to plot the support vectors of LinearSVC.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries for this lab. We will use NumPy, Matplotlib, make_blobs, LinearSVC, and DecisionBoundaryDisplay libraries.

### Step 2: Generate Data

We will generate some random data using the `make_blobs()` function from Scikit-learn. This function generates Gaussian blobs for clustering. We will generate 40 samples with 2 centers.

### Step 3: Plot Data

We will plot the generated data using Matplotlib. The `scatter()` function is used to plot the data.

### Step 4: Train LinearSVC

We will train the LinearSVC model with two different regularization parameters. The hinge loss function is used for training the model. We will use the `fit()` function to train the model.

### Step 5: Obtain Support Vectors

The support vectors are the samples that lie within the margin boundaries, whose size is conventionally constrained to 1. We can obtain the support vectors through the decision function. We will use the `decision_function()` function to obtain the decision function of the model. We will then calculate the support vectors from the decision function.

### Step 6: Plot Support Vectors

We will plot the support vectors on the same plot as the data. We will use the `scatter()` function to plot the support vectors.

### Step 7: Display Decision Boundary

We will display the decision boundary on the plot. We will use the `DecisionBoundaryDisplay` class to display the decision boundary.

### Step 8: Show the Plot

Finally, we will show the plot with support vectors and decision boundary.

## Summary

In this lab, we learned how to plot the support vectors of LinearSVC. We used the `decision_function()` function to obtain the decision function of the model and then calculated the support vectors from the decision function. We also learned how to display the decision boundary on the plot using the `DecisionBoundaryDisplay` class.
