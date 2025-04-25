# 稀疏编码

我们将使用不同方法对信号执行稀疏编码，并可视化结果。

```python
# 按以下格式列出不同的稀疏编码方法：
# (标题，变换算法，变换α,
#  变换非零系数数量，颜色)
estimators = [
    ("正交匹配追踪（OMP）", "omp", None, 15, "海军蓝"),
    ("套索（Lasso）", "lasso_lars", 2, None, "青绿色"),
]
lw = 2

plt.figure(figsize=(13, 6))
for subplot, (D, title) in enumerate(
    zip((D_fixed, D_multi), ("固定宽度", "多种宽度"))
):
    plt.subplot(1, 2, subplot + 1)
    plt.title("针对 %s 字典的稀疏编码" % 标题)
    plt.plot(y, lw=lw, linestyle="--", label="原始信号")
    # 进行小波逼近
    for title, algo, alpha, n_nonzero, color in estimators:
        coder = SparseCoder(
            dictionary=D,
            transform_n_nonzero_coefs=n_nonzero,
            transform_alpha=alpha,
            transform_algorithm=algo,
        )
        x = coder.transform(y.reshape(1, -1))
        density = len(np.flatnonzero(x))
        x = np.ravel(np.dot(x, D))
        squared_error = np.sum((y - x) ** 2)
        plt.plot(
            x,
            color=color,
            lw=lw,
            label="%s: %s 个非零系数，\n%.2f 误差" % (标题, density, squared_error),
        )

    # 软阈值去偏
    coder = SparseCoder(
        dictionary=D, transform_algorithm="threshold", transform_alpha=20
    )
    x = coder.transform(y.reshape(1, -1))
    _, idx = np.where(x!= 0)
    x[0, idx], _, _, _ = np.linalg.lstsq(D[idx, :].T, y, rcond=None)
    x = np.ravel(np.dot(x, D))
    squared_error = np.sum((y - x) ** 2)
    plt.plot(
        x,
        color="深橙色",
        lw=lw,
        label="带去偏的阈值处理:\n%d 个非零系数，%.2f 误差"
        % (len(idx), squared_error),
    )
    plt.axis("tight")
    plt.legend(shadow=False, loc="最佳")
plt.subplots_adjust(0.04, 0.07, 0.97, 0.90, 0.09, 0.2)
plt.show()
```
