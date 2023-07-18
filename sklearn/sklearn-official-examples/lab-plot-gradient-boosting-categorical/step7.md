# Limiting the Number of Splits

We will re-run the same analysis with under-fitting models where we artificially limit the total number of splits by both limiting the number of trees and the depth of each tree.

```python
for pipe in (hist_dropped, hist_one_hot, hist_ordinal, hist_native):
    pipe.set_params(
        histgradientboostingregressor__max_depth=3,
        histgradientboostingregressor__max_iter=15,
    )

dropped_result = cross_validate(hist_dropped, X, y, cv=n_cv_folds, scoring=scoring)
one_hot_result = cross_validate(hist_one_hot, X, y, cv=n_cv_folds, scoring=scoring)
ordinal_result = cross_validate(hist_ordinal, X, y, cv=n_cv_folds, scoring=scoring)
native_result = cross_validate(hist_native, X, y, cv=n_cv_folds, scoring=scoring)

plot_results("Gradient Boosting on Ames Housing (few and small trees)")
```
