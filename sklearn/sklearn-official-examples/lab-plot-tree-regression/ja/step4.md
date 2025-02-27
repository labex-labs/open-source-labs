# 予測する

0から5までの値の範囲で予測を行うためにモデルを使用します。

```python
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
```
