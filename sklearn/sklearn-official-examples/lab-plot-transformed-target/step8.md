# Train and evaluate a linear regression model on the original targets for Ames housing data

We train and evaluate a linear regression model on the original targets for Ames housing data.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("\nLinear Regression on original targets:")
for key, val in score.items():
    print(f"{key}: {val}")
```


