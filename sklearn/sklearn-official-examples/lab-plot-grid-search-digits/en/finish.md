# Summary

In this lab, we learned how to perform hyperparameter tuning with cross-validation using the scikit-learn library. We used the digits dataset and defined a custom refit strategy to select the best candidate from the `cv_results_` attribute of the `GridSearchCV` instance. Finally, we evaluated the fine-tuned model on the left-out evaluation set.
