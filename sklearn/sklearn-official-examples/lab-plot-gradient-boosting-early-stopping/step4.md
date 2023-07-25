# Build and Train the Model with Early Stopping

We will now build and train a gradient boosting model with early stopping. We specify a validation*fraction which denotes the fraction of the whole dataset that will be kept aside from training to assess the validation loss of the model. The gradient boosting model is trained using the training set and evaluated using the validation set. When each additional stage of regression tree is added, the validation set is used to score the model. This is continued until the scores of the model in the last n_iter_no_change stages do not improve by at least tol. After that, the model is considered to have converged and further addition of stages is "stopped early". The number of stages of the final model is available at the attribute n_estimators*.

```python
gbes = ensemble.GradientBoostingClassifier(
        n_estimators=n_estimators,
        validation_fraction=0.2,
        n_iter_no_change=5,
        tol=0.01,
        random_state=0,
    )
start = time.time()
gbes.fit(X_train, y_train)
time_gbes.append(time.time() - start)
```
