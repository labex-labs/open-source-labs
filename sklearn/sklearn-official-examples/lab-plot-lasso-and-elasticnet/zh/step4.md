# 弹性网络（ElasticNet）

弹性网络（ElasticNet）是套索（Lasso）回归和岭回归之间的一种折中方法，因为它结合了 L1 和 L2 惩罚。正则化的程度由两个超参数 `l1_ratio` 和 `alpha` 控制。对于 `l1_ratio = 0`，惩罚是纯粹的 L2 惩罚，模型等同于岭回归。类似地，`l1_ratio = 1` 是纯粹的 L1 惩罚，模型等同于套索回归。对于 `0 < l1_ratio < 1`，惩罚是 L1 和 L2 的组合。

```python
from sklearn.linear_model import ElasticNet

t0 = time()
enet = ElasticNet(alpha=0.08, l1_ratio=0.5).fit(X_train, y_train)
print(f"弹性网络（ElasticNet）拟合完成，耗时{(time() - t0):.3f}秒")

y_pred_enet = enet.predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)
print(f"弹性网络（ElasticNet）在测试数据上的 R 平方值 : {r2_score_enet:.3f}")
```
