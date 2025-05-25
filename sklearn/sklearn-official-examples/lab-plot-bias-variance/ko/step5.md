# 모델 학습 및 기대 평균 제곱 오차 계산

여러 학습 데이터셋에서 모델들을 반복적으로 학습하고, 편향, 분산, 노이즈 항으로 분해하여 기대 평균 제곱 오차를 계산합니다. 또한, 모델 예측과 편향 - 분산 분해를 시각화합니다.

```python
plt.figure(figsize=(10, 8))

# 비교할 추정자 반복
for n, (name, estimator) in enumerate(estimators):
    # 예측 계산
    y_predict = np.zeros((n_test, n_repeat))

    for i in range(n_repeat):
        estimator.fit(X_train[i], y_train[i])
        y_predict[:, i] = estimator.predict(X_test)

    # 평균 제곱 오차의 편향^2 + 분산 + 노이즈 분해
    y_error = np.zeros(n_test)

    for i in range(n_repeat):
        for j in range(n_repeat):
            y_error += (y_test[:, j] - y_predict[:, i]) ** 2

    y_error /= n_repeat * n_repeat

    y_noise = np.var(y_test, axis=1)
    y_bias = (f(X_test) - np.mean(y_predict, axis=1)) ** 2
    y_var = np.var(y_predict, axis=1)

    print(
        "{0}: {1:.4f} (오차) = {2:.4f} (편향^2) "
        " + {3:.4f} (분산) + {4:.4f} (노이즈)".format(
            name, np.mean(y_error), np.mean(y_bias), np.mean(y_var), np.mean(y_noise)
        )
    )

    # 그림 출력
    plt.subplot(2, n_estimators, n + 1)
    plt.plot(X_test, f(X_test), "b", label="$f(x)$")
    plt.plot(X_train[0], y_train[0], ".b", label="LS ~ $y = f(x)+noise$")

    for i in range(n_repeat):
        if i == 0:
            plt.plot(X_test, y_predict[:, i], "r", label=r"$\^y(x)$")
        else:
            plt.plot(X_test, y_predict[:, i], "r", alpha=0.05)

    plt.plot(X_test, np.mean(y_predict, axis=1), "c", label=r"$\mathbb{E}_{LS} \^y(x)$")

    plt.xlim([-5, 5])
    plt.title(name)

    if n == n_estimators - 1:
        plt.legend(loc=(1.1, 0.5))

    plt.subplot(2, n_estimators, n_estimators + n + 1)
    plt.plot(X_test, y_error, "r", label="$오차 (x)$")
    plt.plot(X_test, y_bias, "b", label="$편향^2(x)$"),
    plt.plot(X_test, y_var, "g", label="$분산 (x)$"),
    plt.plot(X_test, y_noise, "c", label="$노이즈 (x)$")

    plt.xlim([-5, 5])
    plt.ylim([0, 0.1])

    if n == n_estimators - 1:
        plt.legend(loc=(1.1, 0.5))

plt.subplots_adjust(right=0.75)
plt.show()
```
