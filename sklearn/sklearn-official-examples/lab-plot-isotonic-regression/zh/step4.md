# 绘制结果

最后，我们将绘制两个回归模型的结果，以直观展示它们对数据的拟合程度。

```python
segments = [[[i, y[i]], [i, y_[i]]] for i in range(n)]
lc = LineCollection(segments, zorder=0)
lc.set_array(np.ones(len(y)))
lc.set_linewidths(np.full(n, 0.5))

fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(12, 6))

ax0.plot(x, y, "C0.", markersize=12)
ax0.plot(x, y_, "C1.-", markersize=12)
ax0.plot(x, lr.predict(x[:, np.newaxis]), "C2-")
ax0.add_collection(lc)
ax0.legend(("训练数据", "保序回归拟合", "线性回归拟合"), loc="lower right")
ax0.set_title("对含噪声数据的保序回归拟合 (n = %d)" % n)

x_test = np.linspace(-10, 110, 1000)
ax1.plot(x_test, ir.predict(x_test), "C1-")
ax1.plot(ir.X_thresholds_, ir.y_thresholds_, "C1.", markersize=12)
ax1.set_title("预测函数 (%d 个阈值)" % len(ir.X_thresholds_))

plt.show()
```
