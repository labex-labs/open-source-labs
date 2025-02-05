# Train Classifiers

- Create a logarithmic grid of the `gamma` and `C` parameters using `np.logspace`.
- Split the data into training and testing sets using `StratifiedShuffleSplit`.
- Perform a grid search using `GridSearchCV` to find the best parameters for the SVM model.
- Fit a classifier for all parameters in the 2D version.
