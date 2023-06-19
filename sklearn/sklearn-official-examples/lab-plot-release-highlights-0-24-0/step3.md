# Improved Performance of HistGradientBoosting Estimators

The memory footprint of `HistGradientBoostingRegressor` and `HistGradientBoostingClassifier` has been significantly improved during calls to `fit`. In addition, histogram initialization is now done in parallel which results in slight speed improvements.


