# RBF SVM Parameter Tuning

## Introduction

This lab demonstrates how to tune the parameters of a Radial Basis Function (RBF) kernel SVM. The `gamma` and `C` parameters of the RBF kernel are crucial for the performance of the SVM model. The goal is to choose the optimal values of these parameters that maximize the accuracy of the model.

## Steps

### Step 1: Load and Prepare Data Set

- Load the iris dataset from scikit-learn.
- Separate the data into feature matrix `X` and target vector `y`.
- Standardize the feature matrix `X` using `StandardScaler`.
- Create a simplified version of the dataset for decision function visualization by keeping only the first two features in `X` and sub-sampling the dataset to keep only two classes and make it a binary classification problem.

### Step 2: Train Classifiers

- Create a logarithmic grid of the `gamma` and `C` parameters using `np.logspace`.
- Split the data into training and testing sets using `StratifiedShuffleSplit`.
- Perform a grid search using `GridSearchCV` to find the best parameters for the SVM model.
- Fit a classifier for all parameters in the 2D version.

### Step 3: Visualization

- Visualize the decision function for a variety of parameter values on a simplified classification problem involving only 2 input features and 2 possible target classes (binary classification).
- Visualize the heatmap of the classifier's cross-validation accuracy as a function of `C` and `gamma`.

### Step 4: Interpretation

- Interpret the results of the visualization and choose the optimal values for `C` and `gamma`.

## Summary

This lab demonstrated how to tune the parameters of a Radial Basis Function (RBF) kernel SVM. The `gamma` and `C` parameters of the RBF kernel are crucial for the performance of the SVM model, and the optimal values for these parameters can be found using a combination of grid search and visualization techniques.
