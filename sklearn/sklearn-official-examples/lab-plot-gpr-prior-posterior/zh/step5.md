# 有理二次核

有理二次核定义为：

$$
k(x_i, x_j) = \left( 1 + \frac{\|x_i - x_j\|^2}{2\alpha\ell^2} \right)^{-\alpha}
$$

其中 $\ell$ 是长度尺度参数，$\alpha$ 控制小尺度和大尺度特征的相对权重。

```python
kernel = 1.0 * RationalQuadratic(length_scale=1.0, alpha=0.1, alpha_bounds=(1e-5, 1e15))
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

fig.suptitle("有理二次核", fontsize=18)
plt.tight_layout()
```
