# Radial Basis Function 커널

Radial Basis Function(RBF) 커널은 다음과 같이 정의됩니다.

$$
k(x_i, x_j) = \exp \left( -\frac{\|x_i - x_j\|^2}{2\ell^2} \right)
$$

여기서 $\ell$은 길이 스케일 매개변수입니다.

```python
kernel = 1.0 * RBF(length_scale=1.0, length_scale_bounds=(1e-1, 10.0))
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

fig.suptitle("Radial Basis Function 커널", fontsize=18)
plt.tight_layout()
```
