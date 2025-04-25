# 查看结果

当使用网格搜索对 RBF 核的复杂度/正则化和带宽进行优化时，我们将可视化核岭回归（KRR）和支持向量回归（SVR）的学习模型。

```python
import matplotlib.pyplot as plt

sv_ind = svr.best_estimator_.support_
plt.scatter(
    X[sv_ind],
    y[sv_ind],
    c="r",
    s=50,
    label="SVR 支持向量",
    zorder=2,
    edgecolors=(0, 0, 0),
)
plt.scatter(X[:100], y[:100], c="k", label="数据", zorder=1, edgecolors=(0, 0, 0))
plt.plot(
    X_plot,
    y_svr,
    c="r",
    label="SVR（拟合：%.3f 秒，预测：%.3f 秒）" % (svr_fit, svr_predict),
)
plt.plot(
    X_plot, y_kr, c="g", label="KRR（拟合：%.3f 秒，预测：%.3f 秒）" % (kr_fit, kr_predict)
)
plt.xlabel("数据")
plt.ylabel("目标")
plt.title("SVR 与核岭回归")
_ = plt.legend()
```
