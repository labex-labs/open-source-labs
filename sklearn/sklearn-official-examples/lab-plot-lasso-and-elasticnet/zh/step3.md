# 自动相关性确定（ARD）

自动相关性确定（ARD）回归是套索（Lasso）的贝叶斯版本。如果需要，它可以为所有参数（包括误差方差）生成区间估计。当信号具有高斯噪声时，它是一个合适的选择。

```python
from sklearn.linear_model import ARDRegression

t0 = time()
ard = ARDRegression().fit(X_train, y_train)
print(f"自动相关性确定（ARD）拟合完成，耗时{(time() - t0):.3f}秒")

y_pred_ard = ard.predict(X_test)
r2_score_ard = r2_score(y_test, y_pred_ard)
print(f"自动相关性确定（ARD）在测试数据上的 R 平方值 : {r2_score_ard:.3f}")
```
