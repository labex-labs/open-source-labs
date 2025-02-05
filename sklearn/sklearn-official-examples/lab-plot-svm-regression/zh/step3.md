# 可视化结果

最后，我们通过将支持向量回归（SVR）模型的结果与样本数据集进行对比绘图，来可视化这些结果。我们还绘制了支持向量和其他训练数据。

```python
import matplotlib.pyplot as plt

# 查看结果
lw = 2

内核标签 = ["RBF", "线性", "多项式"]
模型颜色 = ["m", "c", "g"]

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 10), sharey=True)

for ix, svr in enumerate(svrs):
    axes[ix].plot(
        X,
        svr.predict(X),
        color=模型颜色[ix],
        lw=lw,
        label="{} 模型".format(内核标签[ix])
    )
    axes[ix].scatter(
        X[svr.support_],
        y[svr.support_],
        facecolor="none",
        edgecolor=模型颜色[ix],
        s=50,
        label="{} 支持向量".format(内核标签[ix])
    )
    axes[ix].scatter(
        X[np.setdiff1d(np.arange(len(X)), svr.support_)],
        y[np.setdiff1d(np.arange(len(X)), svr.support_)],
        facecolor="none",
        edgecolor="k",
        s=50,
        label="其他训练数据"
    )
    axes[ix].legend(
        loc="upper center",
        bbox_to_anchor=(0.5, 1.1),
        ncol=1,
        fancybox=True,
        shadow=True
    )

fig.text(0.5, 0.04, "数据", ha="center", va="center")
fig.text(0.06, 0.5, "目标", ha="center", va="center", rotation="vertical")
fig.suptitle("支持向量回归", fontsize=14)
plt.show()
```
