# 予測

このステップでは、前のステップで作成したモデルを使って予測を行います。-100から100までの間隔0.01の新しい値の配列を`np.arange`を使って作成し、その後、モデルの`predict`メソッドを使って出力を予測します。

```python
# Predict
X_test = np.arange(-100.0, 100.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
y_3 = regr_3.predict(X_test)
```
