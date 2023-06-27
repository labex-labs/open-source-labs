# Print Best Parameters and Score

We will print the best parameters and score obtained from the GridSearchCV.

```python
print("Best parameter (CV score=%0.3f):" % search.best_score_)
print(search.best_params_)
```
