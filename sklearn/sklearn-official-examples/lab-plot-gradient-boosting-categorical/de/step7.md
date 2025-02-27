# Begrenzung der Anzahl der Aufteilungen

Wir werden die gleiche Analyse mit unteranpassenden Modellen wiederholen, bei denen wir die Gesamtzahl der Aufteilungen künstlich begrenzen, indem wir sowohl die Anzahl der Bäume als auch die Tiefe jedes Baumes begrenzen.

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

plot_results("Gradient Boosting auf Ames Housing (wenige und kleine Bäume)")
```
