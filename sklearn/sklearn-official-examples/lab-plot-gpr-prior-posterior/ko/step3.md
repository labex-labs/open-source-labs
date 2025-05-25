# 보조 함수

가우시안 프로세스에 사용 가능한 각 개별 커널을 제시하기 전에 가우시안 프로세스에서 추출된 샘플을 플롯할 수 있는 보조 함수를 정의합니다.

```python
def plot_gpr_samples(gpr_model, n_samples, ax):
    """가우시안 프로세스 모델에서 추출된 샘플을 플롯합니다.

    가우시안 프로세스 모델이 학습되지 않았다면 추출된 샘플은 사전 분포에서 추출됩니다. 그렇지 않으면 샘플은 사후 분포에서 추출됩니다. 여기서 샘플은 함수에 해당한다는 점에 유의하십시오.

    매개변수
    ----------
    gpr_model : `GaussianProcessRegressor`
        :class:`~sklearn.gaussian_process.GaussianProcessRegressor` 모델.
    n_samples : int
        가우시안 프로세스 분포에서 추출할 샘플 수.
    ax : matplotlib 축
        샘플을 플롯할 matplotlib 축.
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
            label=f"Sampled function #{idx + 1}",
        )
    ax.plot(x, y_mean, color="black", label="Mean")
    ax.fill_between(
        x,
        y_mean - y_std,
        y_mean + y_std,
        alpha=0.1,
        color="black",
        label=r"$\pm$ 1 std. dev.",
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim([-3, 3])
```
