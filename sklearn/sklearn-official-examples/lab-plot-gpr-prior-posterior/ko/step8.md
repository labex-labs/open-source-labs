# Matérn 커널

Matérn 커널은 다음과 같이 정의됩니다.

$$
k(x_i, x_j) = \frac{1}{\Gamma(\nu)2^{\nu-1}}\left(\frac{\sqrt{2\nu}}{\ell}\|x_i - x_j\|\right)^\nu K_\nu\left(\frac{\sqrt{2\nu}}{\ell}\|x_i - x_j\|\right)
$$

여기서 $\ell$은 길이 스케일 매개변수이고, $\nu$는 함수의 매끄러움을 제어합니다.

```python
kernel = 1.0 * Matern(length_scale=1.0, length_scale_bounds=(1e-1, 10.0), nu=1.5)
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

fig.suptitle("Matérn 커널", fontsize=18)
plt.tight_layout()
```
