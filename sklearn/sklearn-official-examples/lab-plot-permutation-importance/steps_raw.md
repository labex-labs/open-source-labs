# Permutation Importance vs Random Forest Feature Importance (MDI)

## Introduction

In machine learning, feature importance is a valuable tool for understanding which features have the most impact on the target variable. In this lab, we will compare two methods of calculating feature importance: impurity-based feature importance and permutation importance. We will use a random forest classifier on the Titanic dataset to illustrate the differences between the two methods.

## Steps

### Step 1: Data Loading and Feature Engineering

We will use pandas to load a copy of the Titanic dataset. We will also add two random variables that are not correlated with the target variable. We will preprocess the data using `OrdinalEncoder` and `SimpleImputer`.

### Step 2: Define and Train Random Forest Classifier

We will define a random forest classifier using `RandomForestClassifier` and train it on the preprocessed data.

### Step 3: Evaluate Model Accuracy

We will evaluate the accuracy of the random forest classifier on the training and test sets.

### Step 4: Tree's Feature Importance from Mean Decrease in Impurity (MDI)

We will calculate the impurity-based feature importance of the random forest classifier. We will observe that this method can inflate the importance of numerical features.

### Step 5: Permutation Importances on Test Set

We will calculate the permutation importances of the random forest classifier on a held-out test set. We will observe that this method is not biased towards high cardinality features and is a better indicator of feature importance.

### Step 6: Permutation Importances on Training Set

We will calculate the permutation importances of the random forest classifier on the training set. We will observe that the importance of the random numerical and categorical features decreases when the capacity of the trees to overfit is limited.

### Step 7: Permutation Importances on Lower Capacity Model

We will set `min_samples_leaf` to 20 and train the random forest classifier again. We will calculate the permutation importances of the random forest classifier on the training and test sets. We will observe that the importance of the non-predictive random numerical and categorical features decreases further.

## Summary

In this lab, we compared impurity-based feature importance with permutation importance on the Titanic dataset using a random forest classifier. We observed that impurity-based feature importance can inflate the importance of numerical features and is biased towards high cardinality features. Permutation importance is a better indicator of feature importance and is not biased towards high cardinality features. We also observed that limiting the capacity of the trees to overfit can decrease the importance of non-predictive features.
