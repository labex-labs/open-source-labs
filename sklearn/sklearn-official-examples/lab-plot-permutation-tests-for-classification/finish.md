# Summary

In this lab, we learned how to use the `permutation_test_score` function from `sklearn.model_selection` to evaluate the significance of a cross-validated score using permutations. We generated a null distribution by calculating the accuracy of the classifier on 1000 different permutations of the dataset, and calculated an empirical p-value as the percentage of permutations for which the score obtained is greater than the score obtained using the original data. We also plotted the results to visualize the null distribution and the score obtained on the original data.
