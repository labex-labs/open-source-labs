# 早期終了なしでモデルを構築して訓練する

ここでは、早期終了なしで勾配ブースティングモデルを構築して訓練します。

```python
gb = ensemble.GradientBoostingClassifier(n_estimators=n_estimators, random_state=0)
start = time.time()
gb.fit(X_train, y_train)
time_gb.append(time.time() - start)
```
