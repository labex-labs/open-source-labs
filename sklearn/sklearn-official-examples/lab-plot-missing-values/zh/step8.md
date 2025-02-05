# 绘制结果

最后，我们将可视化分数：

```python
n_bars = len(mses_diabetes)
xval = np.arange(n_bars)

colors = ["r", "g", "b", "orange", "black"]

# 绘制糖尿病数据集的结果
plt.figure(figsize=(12, 6))
ax1 = plt.subplot(121)
for j in xval:
    ax1.barh(
        j,
        mses_diabetes[j],
        xerr=stds_diabetes[j],
        color=colors[j],
        alpha=0.6,
        align="center",
    )

ax1.set_title("糖尿病数据集的插补技术")
ax1.set_xlim(left=np.min(mses_diabetes) * 0.9, right=np.max(mses_diabetes) * 1.1)
ax1.set_yticks(xval)
ax1.set_xlabel("均方误差")
ax1.invert_yaxis()
ax1.set_yticklabels(x_labels)

# 绘制加利福尼亚数据集的结果
ax2 = plt.subplot(122)
for j in xval:
    ax2.barh(
        j,
        mses_california[j],
        xerr=stds_california[j],
        color=colors[j],
        alpha=0.6,
        align="center",
    )

ax2.set_title("加利福尼亚数据集的插补技术")
ax2.set_yticks(xval)
ax2.set_xlabel("均方误差")
ax2.invert_yaxis()
ax2.set_yticklabels([""] * n_bars)

plt.show()
```
