# 辅助函数

在介绍高斯过程可用的每个单独核之前，我们将定义一个辅助函数，用于绘制从高斯过程中抽取的样本。

```python
def plot_gpr_samples(gpr_model, n_samples, ax):
    """绘制从高斯过程模型中抽取的样本。

    如果高斯过程模型未训练，则抽取的样本是从先验分布中抽取的。否则，样本是从后验分布中抽取的。请注意，这里的一个样本对应一个函数。

    参数
    ----------
    gpr_model : `GaussianProcessRegressor`
        一个 :class:`~sklearn.gaussian_process.GaussianProcessRegressor` 模型。
    n_samples : int
        要从高斯过程分布中抽取的样本数量。
    ax : matplotlib 轴
        绘制样本的 matplotlib 轴。
    """
    x = np.linspace(0, 5, 100)
    X = x.reshape(-1, 1)

    y_mean, y_std = gpr_model.predict(X, return_std=True)
    y_samples = gpr_model.sample_y(X, n_samples)

    for idx, single_prior in enumerate(y_samples.T):
        ax.plot(
            x,
            single_prior,
            linestyle="--",
            alpha=0.7,
            label=f"采样函数 #{idx + 1}"
        )
    ax.plot(x, y_mean, color="black", label="均值")
    ax.fill_between(
        x,
        y_mean - y_std,
        y_mean + y_std,
        alpha=0.1,
        color="black",
        label=r"$\pm$ 1 标准差"
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim([-3, 3])
```
