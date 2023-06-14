# Summary

In this lab, we compared randomized search and grid search for hyperparameter optimization of a linear SVM model with SGD training. We found that both methods explored the same hyperparameter space, but randomized search was significantly faster. The best hyperparameters found by each method were similar in performance, but randomized search may have slightly worse performance due to noise. In practice, we would not search over so many hyperparameters simultaneously, but only the most important ones.
