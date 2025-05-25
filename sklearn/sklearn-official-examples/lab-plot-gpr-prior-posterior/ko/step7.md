# 내적 커널

내적 커널은 다음과 같이 정의됩니다.

$$
k(x_i, x_j) = (\sigma_0 + x_i^T x_j)^2
$$

여기서 $\sigma_0$은 상수입니다.

```python
kernel = ConstantKernel(0.1, (0.01, 10.0)) * (
    DotProduct(sigma_0=1.0, sigma_0_bounds=(0.1, 10.0)) ** 2
)
gpr = GaussianProcessRegressor(kernel=kernel, random_state=0)

fig, axs = plt.subplots(nrows=2, sharex=True, sharey=True, figsize=(10, 8))

# 사전 분포 샘플 플롯
plot_gpr_samples(gpr, n_samples=n_samples, ax=axs[0])
axs[0].set_title("사전 분포에서의 샘플")

# 사후 분포 샘플 플롯
gpr.fit(X_train, y_train)
plot_gpr_samples(gpr, n_samples=n_samples, ax=axs[1])
axs[1].scatter(X_train[:, 0], y_train, color="red", zorder=10, label="관측값")
axs[1].legend(bbox_to_anchor=(1.05, 1.5), loc="upper left")
axs[1].set_title("사후 분포에서의 샘플")

fig.suptitle("내적 커널", fontsize=18)
plt.tight_layout()
```
