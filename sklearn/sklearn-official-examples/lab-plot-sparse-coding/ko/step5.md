# 희소 코딩

다양한 방법을 사용하여 신호에 대한 희소 코딩을 수행하고 결과를 시각화합니다.

```python
# 다음 형식으로 다양한 희소 코딩 방법을 나열합니다.
# (제목, 변환 알고리즘, 변환 알파,
# 변환 비제로 계수, 색상)
estimators = [
    ("OMP", "omp", None, 15, "navy"),
    ("Lasso", "lasso_lars", 2, None, "turquoise"),
]
lw = 2

plt.figure(figsize=(13, 6))
for subplot, (D, title) in enumerate(
    zip((D_fixed, D_multi), ("고정 너비", "여러 너비"))
):
    plt.subplot(1, 2, subplot + 1)
    plt.title("%s 사전에 대한 희소 코딩" % title)
    plt.plot(y, lw=lw, linestyle="--", label="원본 신호")
    # 웨이블릿 근사 수행
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
            label="%s: %s 비제로 계수,\n%.2f 오차" % (title, density, squared_error),
        )

    # 소프트 임계값 편향 제거
    coder = SparseCoder(
        dictionary=D, transform_algorithm="threshold", transform_alpha=20
    )
    x = coder.transform(y.reshape(1, -1))
    _, idx = np.where(x != 0)
    x[0, idx], _, _, _ = np.linalg.lstsq(D[idx, :].T, y, rcond=None)
    x = np.ravel(np.dot(x, D))
    squared_error = np.sum((y - x) ** 2)
    plt.plot(
        x,
        color="darkorange",
        lw=lw,
        label="임계값 적용 편향 제거:\n%d 비제로 계수, %.2f 오차"
        % (len(idx), squared_error),
    )
    plt.axis("tight")
    plt.legend(shadow=False, loc="best")
plt.subplots_adjust(0.04, 0.07, 0.97, 0.90, 0.09, 0.2)
plt.show()
```
