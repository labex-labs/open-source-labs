# 유리 이차 커널

유리 이차 커널은 다음과 같이 정의됩니다.

$$
k(x_i, x_j) = \left( 1 + \frac{\|x_i - x_j\|^2}{2\alpha\ell^2} \right)^{-\alpha}
$$

여기서 $\ell$은 길이 스케일 매개변수이고, $\alpha$는 소규모 및 대규모 특징의 상대적인 가중치를 제어합니다.

```python
kernel = 1.0 * RationalQuadratic(length_scale=1.0, alpha=0.1, alpha_bounds=(1e-5, 1e15))
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

fig.suptitle("유리 이차 커널", fontsize=18)
plt.tight_layout()
```
