# Comparing Different Categorical Encoders

## Introduction

In this lab, we will compare the performance of different categorical encoders on a wine review dataset. We will use the target column 'points' as the target variable to predict. We will compare the following encoders: TargetEncoder, OneHotEncoder, OrdinalEncoder, and dropping the category. We will also look at how to use the native categorical feature support in `HistGradientBoostingRegressor`.

## Steps

### Step 1: Loading Data from OpenML

First, we load the wine reviews dataset using `fetch_openml` function from scikit-learn.datasets module. We will only use a subset of numerical and categorical features in the data. We will use the following subset of numerical and categorical features in the data: `numerical_features = ["price"]` and `categorical_features = ["country", "province", "region_1", "region_2", "variety", "winery"]`.

### Step 2: Training and Evaluating Pipelines with Different Encoders

In this section, we will evaluate pipelines with `HistGradientBoostingRegressor` with different encoding strategies. We will evaluate the models using cross-validation and record the results.

### Step 3: Native Categorical Feature Support

In this section, we build and evaluate a pipeline that uses native categorical feature support in `HistGradientBoostingRegressor`, which only supports up to 255 unique categories. We group the categorical features into low cardinality and high cardinality features. The high cardinality features will be target encoded and the low cardinality features will use the native categorical feature in gradient boosting.

### Step 4: Plotting the Results

In this section, we display the results by plotting the test and train scores.

## Summary

In this lab, we compared the performance of different categorical encoders on a wine review dataset. We also looked at how to use the native categorical feature support in `HistGradientBoostingRegressor`. We found that dropping the categories perform the worst and the target encoders performs the best. The ordinal encoding imposes an arbitrary order to the features which are then treated as numerical values by the `HistGradientBoostingRegressor`. The one-hot encoding scheme would have likely made the pipeline overfitting as the number of features explodes with rare category occurrences that are correlated with the target by chance. When using the target encoder, the same binning happens, but since the encoded values are statistically ordered by marginal association with the target variable, the binning use by the `HistGradientBoostingRegressor` makes sense and leads to good results.
