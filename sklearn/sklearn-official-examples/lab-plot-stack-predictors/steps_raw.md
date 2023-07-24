# Combine Predictors Using Stacking

## Introduction

In this lab, we will be using the Stacking method to blend several estimators to make predictions. In this strategy, some estimators are individually fitted on some training data while a final estimator is trained using the stacked predictions of these base estimators. We will be using the Ames Housing dataset to predict the final logarithmic price of the houses. We will use 3 learners, linear and non-linear and use a ridge regressor to combine their outputs together. We will also compare the performance of each individual predictor as well as of the stack of the regressors.

## Steps

### Step 1: Download the dataset

We will use the Ames Housing dataset which was first compiled by Dean De Cock and became better known after it was used in Kaggle challenge. It is a set of 1460 residential homes in Ames, Iowa, each described by 80 features. We will use it to predict the final logarithmic price of the houses. In this example we will use only 20 most interesting features chosen using GradientBoostingRegressor() and limit number of entries.

### Step 2: Make pipeline to preprocess the data

Before we can use the Ames dataset we still need to do some preprocessing. First, we will select the categorical and numerical columns of the dataset to construct the first step of the pipeline. Then, we will need to design preprocessing pipelines which depend on the ending regressor. If the ending regressor is a linear model, one needs to one-hot encode the categories. If the ending regressor is a tree-based model an ordinal encoder will be sufficient. Besides, numerical values need to be standardized for a linear model while the raw numerical data can be treated as is by a tree-based model. However, both models need an imputer to handle missing values.

### Step 3: Stack of predictors on a single data set

Now we can use Ames Housing dataset to make the predictions. We check the performance of each individual predictor as well as of the stack of the regressors. We combine 3 learners (linear and non-linear) and use a ridge regressor to combine their outputs together. The stacked regressor will combine the strengths of the different regressors. However, we also see that training the stacked regressor is much more computationally expensive.

### Step 4: Measure and plot the results

We will measure and plot the results of the stacked regressor against the individual predictors.

## Summary

In this lab, we learned about the Stacking method to blend several estimators to make predictions. We used the Ames Housing dataset to predict the final logarithmic price of the houses. We also learned how to design preprocessing pipelines which depend on the ending regressor and how to measure the performance of each individual predictor as well as of the stack of the regressors.
