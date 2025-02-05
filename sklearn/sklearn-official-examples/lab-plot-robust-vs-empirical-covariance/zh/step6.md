# 可视化结果

在这一步中，我们将稳健和经验协方差估计的结果进行可视化。

```python
# 可视化结果
fig, ax = plt.subplots()

# 绘制数据集
内点索引 = np.arange(n_samples)[~np.in1d(np.arange(n_samples), 异常值索引)]
ax.scatter(
    X[内点索引, 0], X[内点索引, 1], color="black", label="内点"
)
ax.scatter(X[异常值索引, 0], X[异常值索引, 1], color="red", label="异常值")

# 绘制估计的协方差矩阵
for 协方差, 颜色, 标签 in zip(
    [emp_cov, robust_cov], ["green", "magenta"], ["MLE", "MCD"]
):
    v, w = np.linalg.eigh(协方差)
    u = w[0] / np.linalg.norm(w[0])
    角度 = np.arctan2(u[1], u[0])
    角度 = 180 * 角度 / np.pi
    v = 2.0 * np.sqrt(2.0) * np.sqrt(v)
    ell = mpl.patches.Ellipse(
        mcd.location_,
        v[0],
        v[1],
        180 + 角度,
        color=颜色,
        label=标签,
        alpha=0.2,
    )
    ell.set_clip_box(ax.bbox)
    ell.set_facecolor(颜色)
    ax.add_artist(ell)

# 设置绘图选项
plt.legend()
plt.title("稳健协方差估计")
plt.show()
```
