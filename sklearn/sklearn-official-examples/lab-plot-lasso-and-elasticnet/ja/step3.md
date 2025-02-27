# Automatic Relevance Determination (ARD)

ARD 回帰は、Lasso のベイジアン版です。必要に応じて、誤差分散を含むすべてのパラメータに対する区間推定を生成することができます。信号にガウスノイズが含まれている場合に適したオプションです。

```python
from sklearn.linear_model import ARDRegression

t0 = time()
ard = ARDRegression().fit(X_train, y_train)
print(f"ARD fit done in {(time() - t0):.3f}s")

y_pred_ard = ard.predict(X_test)
r2_score_ard = r2_score(y_test, y_pred_ard)
print(f"ARD r^2 on test data : {r2_score_ard:.3f}")
```
