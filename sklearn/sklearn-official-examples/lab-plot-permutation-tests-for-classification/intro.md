# Introduction

In machine learning, we often evaluate the performance of a classification model using a score. However, we also need to test the significance of the score to ensure that the model performance is not just by chance. This is where permutation test score comes in handy. It generates a null distribution by calculating the accuracy of the classifier on 1000 different permutations of the dataset. An empirical p-value is then calculated as the percentage of permutations for which the score obtained is greater than the score obtained using the original data. In this lab, we will use the `permutation_test_score` function from `sklearn.model_selection` to evaluate the significance of a cross-validated score using permutations.

> You can write code in `plot-permutation-tests-for-classification.ipynb`.
