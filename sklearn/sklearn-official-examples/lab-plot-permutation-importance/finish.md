# Summary

In this lab, we compared impurity-based feature importance with permutation importance on the Titanic dataset using a random forest classifier. We observed that impurity-based feature importance can inflate the importance of numerical features and is biased towards high cardinality features. Permutation importance is a better indicator of feature importance and is not biased towards high cardinality features. We also observed that limiting the capacity of the trees to overfit can decrease the importance of non-predictive features.
