# Train the Pipeline

We will now train the pipeline on the training subset using the `fit` method. During training, the `SelectKBest` function will select the 3 most informative features based on the ANOVA F-value, and the `LinearSVC` function will train a linear SVM classifier on the selected features.

```python
anova_svm.fit(X_train, y_train)
```


