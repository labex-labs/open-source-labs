# Dimensionality Reduction with Neighborhood Components Analysis

## Introduction

This lab demonstrates how to apply Neighborhood Components Analysis (NCA) for dimensionality reduction using the scikit-learn library. This lab compares NCA with other (linear) dimensionality reduction methods applied on the Digits data set. The Digits dataset contains images of digits from 0 to 9 with approximately 180 samples of each class.

## Steps

### Step 1: Import Libraries

Import the necessary libraries:

- numpy
- matplotlib.pyplot
- datasets
- train_test_split
- PCA
- LinearDiscriminantAnalysis
- KNeighborsClassifier
- NeighborhoodComponentsAnalysis
- make_pipeline
- StandardScaler

### Step 2: Load Digits dataset

Load the Digits dataset using the `load_digits()` function from scikit-learn.

### Step 3: Split dataset

Split the dataset into training and testing datasets using the `train_test_split()` function from scikit-learn.

### Step 4: Define variables

Define the variables needed for the analysis:

- `dim` = number of features in the dataset
- `n_classes` = number of classes in the dataset
- `n_neighbors` = number of neighbors for the KNN classifier
- `random_state` = random state for reproducibility

### Step 5: Dimensionality reduction with PCA

Reduce the dimension of the dataset to 2 using Principal Component Analysis (PCA) by creating a pipeline with `StandardScaler()` and `PCA(n_components=2, random_state=random_state)`.

### Step 6: Dimensionality reduction with Linear Discriminant Analysis

Reduce the dimension of the dataset to 2 using Linear Discriminant Analysis (LDA) by creating a pipeline with `StandardScaler()` and `LinearDiscriminantAnalysis(n_components=2)`.

### Step 7: Dimensionality reduction with Neighborhood Components Analysis

Reduce the dimension of the dataset to 2 using Neighborhood Components Analysis (NCA) by creating a pipeline with `StandardScaler()` and `NeighborhoodComponentsAnalysis(n_components=2, random_state=random_state)`.

### Step 8: Use KNN classifier to evaluate methods

Create a KNeighborsClassifier with `n_neighbors` as the parameter.

### Step 9: Create list of methods to be compared

Create a list of methods to be compared with the KNN classifier using the methods defined in Steps 5-7.

### Step 10: Fit models and evaluate test accuracy

Fit each model and evaluate the test accuracy by transforming the training dataset and the testing dataset with `model.transform()` and fitting the KNN classifier on the transformed training dataset. Compute the nearest neighbor accuracy on the transformed testing dataset using `knn.score()`.

### Step 11: Plot the projected points and show evaluation score

Plot the projected points and show the evaluation score for each method using `plt.scatter()` and `plt.title()`.

### Step 12: Display plots

Display the plots using `plt.show()`.

## Summary

This lab demonstrated how to perform dimensionality reduction with Neighborhood Components Analysis (NCA) and compared it with other (linear) dimensionality reduction methods applied on the Digits data set. The results showed that NCA enforces a clustering of the data that is visually meaningful despite the large reduction in dimension.
