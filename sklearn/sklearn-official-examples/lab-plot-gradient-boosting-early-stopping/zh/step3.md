# 不使用早期停止构建并训练模型

现在我们将构建并训练一个不使用早期停止的梯度提升模型。

```python
gb = ensemble.GradientBoostingClassifier(n_estimators=n_estimators, random_state=0)
start = time.time()
gb.fit(X_train, y_train)
time_gb.append(time.time() - start)
```
