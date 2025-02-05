# Calculate permutation feature importance

Now, we will calculate the permutation feature importance using the `permutation_importance` function from scikit-learn. This function takes as input the trained model, the validation set, and the number of times the features should be permuted.

```python
from sklearn.inspection import permutation_importance

# Calculate permutation feature importance
result = permutation_importance(model, X_val, y_val, n_repeats=30, random_state=0)

# Print the feature importances
for i in result.importances_mean.argsort()[::-1]:
    if result.importances_mean[i] - 2 * result.importances_std[i] > 0:
        print(f"{diabetes.feature_names[i]}: {result.importances_mean[i]:.3f} +/- {result.importances_std[i]:.3f}")
```
