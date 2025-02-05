# 点积核

点积核定义为：

$$
k(x_i, x_j) = (\sigma_0 + x_i^T x_j)^2
$$

其中 $\sigma_0$ 是一个常数。

```python
kernel = ConstantKernel(0.1, (0.01, 10.0)) * (
    DotProduct(sigma_0=1.0, sigma_0_bounds=(0.1, 10.0)) ** 2
)
gpr = GaussianProcessRegressor(kernel=kernel, random_state=0)

fig, axs = plt.subplots(nrows=2, sharex=True, sharey=True, figsize=(10, 8))

# 绘制先验
plot_gpr_samples(gpr, n_samples=n_samples, ax=axs[0])
axs[0].set_title("来自先验分布的样本")

# 绘制后验
gpr.fit(X_train, y_train)
plot_gpr_samples(gpr, n_samples=n_samples, ax=axs[1])
axs[1].scatter(X_train[:, 0], y_train, color="red", zorder=10, label="观测值")
axs[1].legend(bbox_to_anchor=(1.05, 1.5), loc="upper left")
axs[1].set_title("来自后验分布的样本")

fig.suptitle("点积核", fontsize=18)
plt.tight_layout()
```
