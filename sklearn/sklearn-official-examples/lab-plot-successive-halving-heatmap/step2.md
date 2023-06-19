# Perform Grid Search

We will use Grid Search to perform parameter search on the SVC model. We will use the generated synthetic dataset and the parameter grid generated in Step 1.

```python
tic = time()
gs = GridSearchCV(estimator=clf, param_grid=param_grid)
gs.fit(X, y)
gs_time = time() - tic
```
